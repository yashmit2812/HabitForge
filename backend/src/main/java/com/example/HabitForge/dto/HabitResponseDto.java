package com.example.HabitForge.dto;

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