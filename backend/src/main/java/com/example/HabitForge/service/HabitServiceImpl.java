package com.example.HabitForge.service;

import com.example.HabitForge.dto.HabitRequestDto;
import com.example.HabitForge.dto.HabitResponseDto;
import com.example.HabitForge.model.Habit;
import com.example.HabitForge.repository.HabitRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.stream.Collectors;

/**
 * Habit Service Implementation.
 *
 * Design Principle - Loose Coupling and Modularity:
 * Interacts with HabitRepository and StreakCalculationService solely through abstractions.
 * Utilizes Spring Constructor Dependency Injection.
 */
@Service
public class HabitServiceImpl implements HabitService {

    private final HabitRepository habitRepository;
    private final StreakCalculationService streakCalculationService;
    private final GamificationService gamificationService;

    @Autowired
    public HabitServiceImpl(HabitRepository habitRepository,
                            StreakCalculationService streakCalculationService,
                            GamificationService gamificationService) {
        this.habitRepository = habitRepository;
        this.streakCalculationService = streakCalculationService;
        this.gamificationService = gamificationService;
    }

    @Override
    public HabitResponseDto createHabit(String userId, HabitRequestDto request) {
        Habit habit = new Habit();
        habit.setUserId(userId);
        habit.setTitle(request.getTitle());
        habit.setDescription(request.getDescription());
        habit.setCategory(request.getCategory());
        habit.setTimeOfDay(request.getTimeOfDay() != null ? request.getTimeOfDay() : "Morning");
        habit.setXpReward(request.getXpReward() > 0 ? request.getXpReward() : 20);
        habit.setHpPenalty(request.getHpPenalty() > 0 ? request.getHpPenalty() : 10);

        Habit saved = habitRepository.save(habit);
        return mapToDto(saved);
    }

    @Override
    public HabitResponseDto getHabitById(String habitId) {
        Habit habit = habitRepository.findById(habitId)
                .orElseThrow(() -> new NoSuchElementException("Habit not found with ID: " + habitId));
        return mapToDto(habit);
    }

    @Override
    public List<HabitResponseDto> getUserHabits(String userId) {
        return habitRepository.findByUserId(userId).stream()
                .map(this::mapToDto)
                .collect(Collectors.toList());
    }

    @Override
    public List<HabitResponseDto> getUserHabitsByTimeOfDay(String userId, String timeOfDay) {
        return habitRepository.findByUserIdAndTimeOfDay(userId, timeOfDay).stream()
                .map(this::mapToDto)
                .collect(Collectors.toList());
    }

    @Override
    public HabitResponseDto completeHabit(String habitId, String userId) {
        Habit habit = habitRepository.findById(habitId)
                .orElseThrow(() -> new NoSuchElementException("Habit not found: " + habitId));

        if (!habit.isCompletedToday()) {
            streakCalculationService.processHabitCompletion(habit, LocalDate.now());
            habitRepository.save(habit);
            gamificationService.awardHabitRewards(userId, habit.getXpReward());
        }

        return mapToDto(habit);
    }

    @Override
    public HabitResponseDto updateHabit(String habitId, HabitRequestDto request) {
        Habit habit = habitRepository.findById(habitId)
                .orElseThrow(() -> new NoSuchElementException("Habit not found: " + habitId));

        habit.setTitle(request.getTitle());
        habit.setDescription(request.getDescription());
        habit.setCategory(request.getCategory());
        habit.setTimeOfDay(request.getTimeOfDay());
        habit.setXpReward(request.getXpReward());
        habit.setHpPenalty(request.getHpPenalty());

        Habit updated = habitRepository.save(habit);
        return mapToDto(updated);
    }

    @Override
    public void deleteHabit(String habitId) {
        habitRepository.deleteById(habitId);
    }

    private HabitResponseDto mapToDto(Habit habit) {
        return new HabitResponseDto(
                habit.getId(),
                habit.getTitle(),
                habit.getDescription(),
                habit.getCategory(),
                habit.getTimeOfDay(),
                habit.getXpReward(),
                habit.getHpPenalty(),
                habit.getCurrentStreak(),
                habit.getLongestStreak(),
                habit.isCompletedToday(),
                habit.getLastCompletedDate()
        );
    }
}