package com.example.HabitForge.model;

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