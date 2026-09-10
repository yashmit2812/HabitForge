package com.example.HabitForge.repository;

import com.example.HabitForge.model.Habit;
import java.util.List;
import java.util.Optional;

/**
 * Habit Data Access Repository Interface.
 *
 * Design Principle - Abstraction & Low Coupling:
 * Hides database-specific details behind standard CRUD methods.
 */
public interface HabitRepository {
    Habit save(Habit habit);
    Optional<Habit> findById(String id);
    List<Habit> findByUserId(String userId);
    List<Habit> findByUserIdAndTimeOfDay(String userId, String timeOfDay);
    void deleteById(String id);
    List<Habit> findAll();
}