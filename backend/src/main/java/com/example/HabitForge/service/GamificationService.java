package com.example.HabitForge.service;

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