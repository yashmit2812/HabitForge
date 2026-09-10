import os
from pathlib import Path

base = Path(r"C:\Yashmit\SE PROJECT\backend\src\main\java\com\example\HabitForge")

files = {
    base / "model" / "User.java": """package com.example.HabitForge.model;

import java.time.LocalDateTime;

/**
 * User Entity Model.
 * Represents an adventurer/player in HabitForge with health, level, and experience mechanics.
 *
 * Design Principle - Modularity:
 * Encapsulates RPG progression metrics (HP, XP, Level, Gold) separate from individual habit tracking.
 */
public class User {
    private String id;
    private String username;
    private String email;
    private int level;
    private int currentHp;
    private int maxHp;
    private int currentXp;
    private int xpToNextLevel;
    private int gold;
    private int totalStreaksActive;
    private LocalDateTime createdAt;

    public User() {
        this.level = 1;
        this.maxHp = 100;
        this.currentHp = 100;
        this.currentXp = 0;
        this.xpToNextLevel = 100;
        this.gold = 50;
        this.totalStreaksActive = 0;
        this.createdAt = LocalDateTime.now();
    }

    public User(String id, String username, String email) {
        this();
        this.id = id;
        this.username = username;
        this.email = email;
    }

    public String getId() { return id; }
    public void setId(String id) { this.id = id; }

    public String getUsername() { return username; }
    public void setUsername(String username) { this.username = username; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public int getLevel() { return level; }
    public void setLevel(int level) { this.level = level; }

    public int getCurrentHp() { return currentHp; }
    public void setCurrentHp(int currentHp) { this.currentHp = Math.max(0, Math.min(currentHp, this.maxHp)); }

    public int getMaxHp() { return maxHp; }
    public void setMaxHp(int maxHp) { this.maxHp = maxHp; }

    public int getCurrentXp() { return currentXp; }
    public void setCurrentXp(int currentXp) { this.currentXp = currentXp; }

    public int getXpToNextLevel() { return xpToNextLevel; }
    public void setXpToNextLevel(int xpToNextLevel) { this.xpToNextLevel = xpToNextLevel; }

    public int getGold() { return gold; }
    public void setGold(int gold) { this.gold = gold; }

    public int getTotalStreaksActive() { return totalStreaksActive; }
    public void setTotalStreaksActive(int totalStreaksActive) { this.totalStreaksActive = totalStreaksActive; }

    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
}
""",

    base / "dto" / "HabitRequestDto.java": """package com.example.HabitForge.dto;

/**
 * Habit Creation/Update Request Data Transfer Object.
 *
 * Design Principle - Abstraction and Loose Coupling:
 * Prevents clients from manipulating internal entity fields directly (e.g. currentStreak, id)
 * and guarantees strict API payload contracts.
 */
public class HabitRequestDto {
    private String title;
    private String description;
    private String category;
    private String timeOfDay;
    private int xpReward;
    private int hpPenalty;

    public HabitRequestDto() {}

    public HabitRequestDto(String title, String description, String category, String timeOfDay, int xpReward, int hpPenalty) {
        this.title = title;
        this.description = description;
        this.category = category;
        this.timeOfDay = timeOfDay;
        this.xpReward = xpReward;
        this.hpPenalty = hpPenalty;
    }

    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }

    public String getCategory() { return category; }
    public void setCategory(String category) { this.category = category; }

    public String getTimeOfDay() { return timeOfDay; }
    public void setTimeOfDay(String timeOfDay) { this.timeOfDay = timeOfDay; }

    public int getXpReward() { return xpReward; }
    public void setXpReward(int xpReward) { this.xpReward = xpReward; }

    public int getHpPenalty() { return hpPenalty; }
    public void setHpPenalty(int hpPenalty) { this.hpPenalty = hpPenalty; }
}
""",

    base / "dto" / "HabitResponseDto.java": """package com.example.HabitForge.dto;

import java.time.LocalDate;

/**
 * Habit Response Data Transfer Object.
 *
 * Design Principle - Abstraction:
 * Exposes a clean, user-friendly presentation model to the frontend client,
 * hiding internal database mappings.
 */
public class HabitResponseDto {
    private String id;
    private String title;
    private String description;
    private String category;
    private String timeOfDay;
    private int xpReward;
    private int hpPenalty;
    private int currentStreak;
    private int longestStreak;
    private boolean completedToday;
    private LocalDate lastCompletedDate;

    public HabitResponseDto() {}

    public HabitResponseDto(String id, String title, String description, String category,
                            String timeOfDay, int xpReward, int hpPenalty, int currentStreak,
                            int longestStreak, boolean completedToday, LocalDate lastCompletedDate) {
        this.id = id;
        this.title = title;
        this.description = description;
        this.category = category;
        this.timeOfDay = timeOfDay;
        this.xpReward = xpReward;
        this.hpPenalty = hpPenalty;
        this.currentStreak = currentStreak;
        this.longestStreak = longestStreak;
        this.completedToday = completedToday;
        this.lastCompletedDate = lastCompletedDate;
    }

    public String getId() { return id; }
    public void setId(String id) { this.id = id; }

    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }

    public String getCategory() { return category; }
    public void setCategory(String category) { this.category = category; }

    public String getTimeOfDay() { return timeOfDay; }
    public void setTimeOfDay(String timeOfDay) { this.timeOfDay = timeOfDay; }

    public int getXpReward() { return xpReward; }
    public void setXpReward(int xpReward) { this.xpReward = xpReward; }

    public int getHpPenalty() { return hpPenalty; }
    public void setHpPenalty(int hpPenalty) { this.hpPenalty = hpPenalty; }

    public int getCurrentStreak() { return currentStreak; }
    public void setCurrentStreak(int currentStreak) { this.currentStreak = currentStreak; }

    public int getLongestStreak() { return longestStreak; }
    public void setLongestStreak(int longestStreak) { this.longestStreak = longestStreak; }

    public boolean isCompletedToday() { return completedToday; }
    public void setCompletedToday(boolean completedToday) { this.completedToday = completedToday; }

    public LocalDate getLastCompletedDate() { return lastCompletedDate; }
    public void setLastCompletedDate(LocalDate lastCompletedDate) { this.lastCompletedDate = lastCompletedDate; }
}
""",

    base / "dto" / "UserStatsDto.java": """package com.example.HabitForge.dto;

/**
 * User Statistics DTO.
 * Summarizes player progression and gamified health state.
 */
public class UserStatsDto {
    private String userId;
    private String username;
    private int level;
    private int currentHp;
    private int maxHp;
    private int currentXp;
    private int xpToNextLevel;
    private int gold;
    private double hpPercentage;
    private double xpPercentage;

    public UserStatsDto() {}

    public UserStatsDto(String userId, String username, int level, int currentHp, int maxHp,
                        int currentXp, int xpToNextLevel, int gold) {
        this.userId = userId;
        this.username = username;
        this.level = level;
        this.currentHp = currentHp;
        this.maxHp = maxHp;
        this.currentXp = currentXp;
        this.xpToNextLevel = xpToNextLevel;
        this.gold = gold;
        this.hpPercentage = maxHp > 0 ? ((double) currentHp / maxHp) * 100.0 : 0.0;
        this.xpPercentage = xpToNextLevel > 0 ? ((double) currentXp / xpToNextLevel) * 100.0 : 0.0;
    }

    public String getUserId() { return userId; }
    public void setUserId(String userId) { this.userId = userId; }

    public String getUsername() { return username; }
    public void setUsername(String username) { this.username = username; }

    public int getLevel() { return level; }
    public void setLevel(int level) { this.level = level; }

    public int getCurrentHp() { return currentHp; }
    public void setCurrentHp(int currentHp) { this.currentHp = currentHp; }

    public int getMaxHp() { return maxHp; }
    public void setMaxHp(int maxHp) { this.maxHp = maxHp; }

    public int getCurrentXp() { return currentXp; }
    public void setCurrentXp(int currentXp) { this.currentXp = currentXp; }

    public int getXpToNextLevel() { return xpToNextLevel; }
    public void setXpToNextLevel(int xpToNextLevel) { this.xpToNextLevel = xpToNextLevel; }

    public int getGold() { return gold; }
    public void setGold(int gold) { this.gold = gold; }

    public double getHpPercentage() { return hpPercentage; }
    public void setHpPercentage(double hpPercentage) { this.hpPercentage = hpPercentage; }

    public double getXpPercentage() { return xpPercentage; }
    public void setXpPercentage(double xpPercentage) { this.xpPercentage = xpPercentage; }
}
""",

    base / "strategy" / "StreakStrategy.java": """package com.example.HabitForge.strategy;

import com.example.HabitForge.model.Habit;
import java.time.LocalDate;

/**
 * Strategy Pattern Interface for Streak Calculation.
 *
 * Design Principle - Abstraction and Loose Coupling:
 * Decouples the streak calculation rules from the HabitService.
 * Allows swapping between DailyStreakStrategy, FlexibleStreakStrategy, or WeekendExemptStrategy
 * without altering client code (Open/Closed Principle).
 */
public interface StreakStrategy {
    int calculateNewStreak(Habit habit, LocalDate completionDate);
    boolean isStreakBroken(Habit habit, LocalDate currentDate);
}
""",

    base / "strategy" / "DailyStreakStrategy.java": """package com.example.HabitForge.strategy;

import com.example.HabitForge.model.Habit;
import org.springframework.stereotype.Component;

import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

/**
 * Concrete Daily Streak Strategy.
 *
 * Design Principle - High Cohesion:
 * Contains strictly the logic for consecutive-day evaluation and resets.
 */
@Component
public class DailyStreakStrategy implements StreakStrategy {

    @Override
    public int calculateNewStreak(Habit habit, LocalDate completionDate) {
        LocalDate lastDate = habit.getLastCompletedDate();
        if (lastDate == null) {
            return 1;
        }

        long daysBetween = ChronoUnit.DAYS.between(lastDate, completionDate);
        if (daysBetween == 0) {
            return habit.getCurrentStreak();
        } else if (daysBetween == 1) {
            return habit.getCurrentStreak() + 1;
        } else {
            return 1;
        }
    }

    @Override
    public boolean isStreakBroken(Habit habit, LocalDate currentDate) {
        LocalDate lastDate = habit.getLastCompletedDate();
        if (lastDate == null) {
            return false;
        }
        long daysBetween = ChronoUnit.DAYS.between(lastDate, currentDate);
        return daysBetween > 1;
    }
}
""",

    base / "repository" / "HabitRepository.java": """package com.example.HabitForge.repository;

import com.example.HabitForge.model.Habit;
import java.util.List;
import java.util.Optional;

/**
 * Habit Data Access Repository Interface.
 *
 * Design Principle - Abstraction & Low Coupling:
 * Hides database-specific details behind standard CRUD methods.
 */
public interface HabitRepository {
    Habit save(Habit habit);
    Optional<Habit> findById(String id);
    List<Habit> findByUserId(String userId);
    List<Habit> findByUserIdAndTimeOfDay(String userId, String timeOfDay);
    void deleteById(String id);
    List<Habit> findAll();
}
""",

    base / "repository" / "InMemoryHabitRepository.java": """package com.example.HabitForge.repository;

import com.example.HabitForge.model.Habit;
import org.springframework.stereotype.Repository;

import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.stream.Collectors;

/**
 * Concrete In-Memory Implementation of HabitRepository.
 * Enables zero-dependency immediate runtime execution while conforming strictly to HabitRepository abstraction.
 */
@Repository
public class InMemoryHabitRepository implements HabitRepository {
    private final Map<String, Habit> store = new ConcurrentHashMap<>();

    public InMemoryHabitRepository() {
        Habit h1 = new Habit("h-1", "user-default", "Morning Meditation and Deep Focus",
                "Perform 15 minutes of mindfulness before checking phone", "Mindfulness", "Morning", 20, 10);
        h1.setCurrentStreak(5);
        h1.setLongestStreak(7);

        Habit h2 = new Habit("h-2", "user-default", "Code 1 Algorithmic Problem",
                "Solve 1 medium data structure or software engineering problem", "Study", "Afternoon", 35, 20);
        h2.setCurrentStreak(12);
        h2.setLongestStreak(12);

        Habit h3 = new Habit("h-3", "user-default", "Evening Strength Workout",
                "45-minute gym session or calisthenics routine", "Fitness", "Evening", 30, 15);
        h3.setCurrentStreak(3);
        h3.setLongestStreak(5);

        store.put(h1.getId(), h1);
        store.put(h2.getId(), h2);
        store.put(h3.getId(), h3);
    }

    @Override
    public Habit save(Habit habit) {
        if (habit.getId() == null || habit.getId().isBlank()) {
            habit.setId(UUID.randomUUID().toString());
        }
        store.put(habit.getId(), habit);
        return habit;
    }

    @Override
    public Optional<Habit> findById(String id) {
        return Optional.ofNullable(store.get(id));
    }

    @Override
    public List<Habit> findByUserId(String userId) {
        return store.values().stream()
                .filter(h -> h.getUserId().equals(userId))
                .collect(Collectors.toList());
    }

    @Override
    public List<Habit> findByUserIdAndTimeOfDay(String userId, String timeOfDay) {
        return store.values().stream()
                .filter(h -> h.getUserId().equals(userId) && h.getTimeOfDay().equalsIgnoreCase(timeOfDay))
                .collect(Collectors.toList());
    }

    @Override
    public void deleteById(String id) {
        store.remove(id);
    }

    @Override
    public List<Habit> findAll() {
        return new ArrayList<>(store.values());
    }
}
""",

    base / "service" / "HabitService.java": """package com.example.HabitForge.service;

import com.example.HabitForge.dto.HabitRequestDto;
import com.example.HabitForge.dto.HabitResponseDto;

import java.util.List;

/**
 * Habit Management Business Interface.
 *
 * Design Principle - Abstraction:
 * Establishes a contract defining what habit operations are available,
 * completely independent of how business logic or storage is executed.
 */
public interface HabitService {
    HabitResponseDto createHabit(String userId, HabitRequestDto request);
    HabitResponseDto getHabitById(String habitId);
    List<HabitResponseDto> getUserHabits(String userId);
    List<HabitResponseDto> getUserHabitsByTimeOfDay(String userId, String timeOfDay);
    HabitResponseDto completeHabit(String habitId, String userId);
    HabitResponseDto updateHabit(String habitId, HabitRequestDto request);
    void deleteHabit(String habitId);
}
""",

    base / "service" / "StreakCalculationService.java": """package com.example.HabitForge.service;

import com.example.HabitForge.model.Habit;
import com.example.HabitForge.strategy.StreakStrategy;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.LocalDate;

/**
 * Streak Calculation Domain Service.
 *
 * Design Principle - High Cohesion and Low Coupling:
 * Has one dedicated responsibility: computing streak updates and resets.
 * Uses constructor dependency injection to receive the StreakStrategy.
 */
@Service
public class StreakCalculationService {

    private final StreakStrategy streakStrategy;

    @Autowired
    public StreakCalculationService(StreakStrategy streakStrategy) {
        this.streakStrategy = streakStrategy;
    }

    public void processHabitCompletion(Habit habit, LocalDate date) {
        int updatedStreak = streakStrategy.calculateNewStreak(habit, date);
        habit.setCurrentStreak(updatedStreak);
        if (updatedStreak > habit.getLongestStreak()) {
            habit.setLongestStreak(updatedStreak);
        }
        habit.setCompletedToday(true);
        habit.setLastCompletedDate(date);
    }

    public void evaluateMidnightPenalty(Habit habit, LocalDate currentDate) {
        if (!habit.isCompletedToday()) {
            if (streakStrategy.isStreakBroken(habit, currentDate)) {
                habit.setCurrentStreak(0);
            }
        }
        habit.setCompletedToday(false);
    }
}
""",

    base / "service" / "GamificationService.java": """package com.example.HabitForge.service;

import com.example.HabitForge.dto.UserStatsDto;
import com.example.HabitForge.model.User;
import org.springframework.stereotype.Service;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

/**
 * Gamification Engine Service.
 *
 * Design Principle - High Cohesion:
 * Dedicated solely to RPG logic: leveling up, health points (HP) deduction,
 * gold economy, and experience points (XP) calculations.
 */
@Service
public class GamificationService {
    private final Map<String, User> userCache = new ConcurrentHashMap<>();

    public GamificationService() {
        User defaultUser = new User("user-default", "Yashmit_Adventurer", "yashmit@vitstudent.ac.in");
        defaultUser.setLevel(4);
        defaultUser.setCurrentHp(85);
        defaultUser.setMaxHp(100);
        defaultUser.setCurrentXp(340);
        defaultUser.setXpToNextLevel(500);
        defaultUser.setGold(120);
        defaultUser.setTotalStreaksActive(3);
        userCache.put(defaultUser.getId(), defaultUser);
    }

    public User getOrCreateUser(String userId) {
        return userCache.computeIfAbsent(userId, id -> new User(id, "Adventurer_" + id, id + "@habitforge.io"));
    }

    public UserStatsDto getUserStats(String userId) {
        User user = getOrCreateUser(userId);
        return new UserStatsDto(user.getId(), user.getUsername(), user.getLevel(),
                user.getCurrentHp(), user.getMaxHp(), user.getCurrentXp(),
                user.getXpToNextLevel(), user.getGold());
    }

    public UserStatsDto awardHabitRewards(String userId, int xpGain) {
        User user = getOrCreateUser(userId);
        user.setCurrentXp(user.getCurrentXp() + xpGain);
        user.setGold(user.getGold() + (xpGain / 2));

        while (user.getCurrentXp() >= user.getXpToNextLevel()) {
            user.setCurrentXp(user.getCurrentXp() - user.getXpToNextLevel());
            user.setLevel(user.getLevel() + 1);
            user.setMaxHp(user.getMaxHp() + 10);
            user.setCurrentHp(user.getMaxHp());
            user.setXpToNextLevel((int) (user.getXpToNextLevel() * 1.25));
        }

        return getUserStats(userId);
    }

    public UserStatsDto deductHpPenalty(String userId, int hpDamage) {
        User user = getOrCreateUser(userId);
        user.setCurrentHp(user.getCurrentHp() - hpDamage);
        return getUserStats(userId);
    }
}
""",

    base / "service" / "HabitServiceImpl.java": """package com.example.HabitForge.service;

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
""",

    base / "controller" / "HabitController.java": """package com.example.HabitForge.controller;

import com.example.HabitForge.dto.HabitRequestDto;
import com.example.HabitForge.dto.HabitResponseDto;
import com.example.HabitForge.service.HabitService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * Habit Management REST Controller.
 *
 * Design Principle - Modularity and Separation of Concerns:
 * Purely responsible for HTTP endpoint binding, serialization, and status codes.
 * Delegates all domain logic to HabitService.
 */
@RestController
@RequestMapping("/api/habits")
@CrossOrigin(origins = "*")
public class HabitController {

    private final HabitService habitService;

    @Autowired
    public HabitController(HabitService habitService) {
        this.habitService = habitService;
    }

    @GetMapping
    public ResponseEntity<List<HabitResponseDto>> getHabits(
            @RequestParam(defaultValue = "user-default") String userId,
            @RequestParam(required = false) String timeOfDay) {
        if (timeOfDay != null && !timeOfDay.isBlank()) {
            return ResponseEntity.ok(habitService.getUserHabitsByTimeOfDay(userId, timeOfDay));
        }
        return ResponseEntity.ok(habitService.getUserHabits(userId));
    }

    @GetMapping("/{id}")
    public ResponseEntity<HabitResponseDto> getHabitById(@PathVariable String id) {
        return ResponseEntity.ok(habitService.getHabitById(id));
    }

    @PostMapping
    public ResponseEntity<HabitResponseDto> createHabit(
            @RequestParam(defaultValue = "user-default") String userId,
            @RequestBody HabitRequestDto request) {
        HabitResponseDto created = habitService.createHabit(userId, request);
        return new ResponseEntity<>(created, HttpStatus.CREATED);
    }

    @PostMapping("/{id}/complete")
    public ResponseEntity<HabitResponseDto> completeHabit(
            @PathVariable String id,
            @RequestParam(defaultValue = "user-default") String userId) {
        return ResponseEntity.ok(habitService.completeHabit(id, userId));
    }

    @PutMapping("/{id}")
    public ResponseEntity<HabitResponseDto> updateHabit(
            @PathVariable String id,
            @RequestBody HabitRequestDto request) {
        return ResponseEntity.ok(habitService.updateHabit(id, request));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteHabit(@PathVariable String id) {
        habitService.deleteHabit(id);
        return ResponseEntity.noContent().build();
    }
}
""",

    base / "controller" / "GamificationController.java": """package com.example.HabitForge.controller;

import com.example.HabitForge.dto.UserStatsDto;
import com.example.HabitForge.service.GamificationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

/**
 * Gamification and Character Stats REST Controller.
 */
@RestController
@RequestMapping("/api/gamification")
@CrossOrigin(origins = "*")
public class GamificationController {

    private final GamificationService gamificationService;

    @Autowired
    public GamificationController(GamificationService gamificationService) {
        this.gamificationService = gamificationService;
    }

    @GetMapping("/stats")
    public ResponseEntity<UserStatsDto> getUserStats(
            @RequestParam(defaultValue = "user-default") String userId) {
        return ResponseEntity.ok(gamificationService.getUserStats(userId));
    }

    @PostMapping("/damage")
    public ResponseEntity<UserStatsDto> applyPenalty(
            @RequestParam(defaultValue = "user-default") String userId,
            @RequestParam(defaultValue = "15") int hpDamage) {
        return ResponseEntity.ok(gamificationService.deductHpPenalty(userId, hpDamage));
    }
}
"""
}

for path, content in files.items():
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip(), encoding="utf-8")
    print(f"Created: {path.name}")

print("Codebase generation complete!")
