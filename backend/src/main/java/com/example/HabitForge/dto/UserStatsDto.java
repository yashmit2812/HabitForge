package com.example.HabitForge.dto;

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