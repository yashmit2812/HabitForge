package com.example.HabitForge.service;

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