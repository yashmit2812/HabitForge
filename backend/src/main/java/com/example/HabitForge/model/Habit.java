package com.example.HabitForge.model;

import java.time.LocalDate;
import java.time.LocalDateTime;

/**
 * Habit Domain Model.
 * Represents a user's quest within HabitForge with RPG gamification attributes.
 *
 * Design Principle - Modularity & Encapsulation:
 * Encapsulates core habit state, streak data, XP/HP stakes, and completion timestamps.
 */
public class Habit {
    private String id;
    private String userId;
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
    private LocalDateTime createdAt;

    public Habit() {
        this.createdAt = LocalDateTime.now();
        this.currentStreak = 0;
        this.longestStreak = 0;
        this.completedToday = false;
    }

    public Habit(String id, String userId, String title, String description, String category,
                 String timeOfDay, int xpReward, int hpPenalty) {
        this();
        this.id = id;
        this.userId = userId;
        this.title = title;
        this.description = description;
        this.category = category;
        this.timeOfDay = timeOfDay;
        this.xpReward = xpReward;
        this.hpPenalty = hpPenalty;
    }

    public String getId() { return id; }
    public void setId(String id) { this.id = id; }

    public String getUserId() { return userId; }
    public void setUserId(String userId) { this.userId = userId; }

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

    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
}
