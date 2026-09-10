package com.example.HabitForge.strategy;

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