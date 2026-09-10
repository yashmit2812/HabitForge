package com.example.HabitForge.strategy;

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