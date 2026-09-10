package com.example.HabitForge.service;

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