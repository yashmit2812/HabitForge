package com.example.HabitForge.dto;

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