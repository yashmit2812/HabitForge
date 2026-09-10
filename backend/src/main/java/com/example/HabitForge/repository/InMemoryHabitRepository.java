package com.example.HabitForge.repository;

import com.example.HabitForge.model.Habit;
import org.springframework.stereotype.Repository;

import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.stream.Collectors;

/**
 * Concrete In-Memory Implementation of HabitRepository.
 * Enables zero-dependency immediate runtime execution while conforming strictly to HabitRepository abstraction.
 */
@Repository
public class InMemoryHabitRepository implements HabitRepository {
    private final Map<String, Habit> store = new ConcurrentHashMap<>();

    public InMemoryHabitRepository() {
        Habit h1 = new Habit("h-1", "user-default", "Morning Meditation and Deep Focus",
                "Perform 15 minutes of mindfulness before checking phone", "Mindfulness", "Morning", 20, 10);
        h1.setCurrentStreak(5);
        h1.setLongestStreak(7);

        Habit h2 = new Habit("h-2", "user-default", "Code 1 Algorithmic Problem",
                "Solve 1 medium data structure or software engineering problem", "Study", "Afternoon", 35, 20);
        h2.setCurrentStreak(12);
        h2.setLongestStreak(12);

        Habit h3 = new Habit("h-3", "user-default", "Evening Strength Workout",
                "45-minute gym session or calisthenics routine", "Fitness", "Evening", 30, 15);
        h3.setCurrentStreak(3);
        h3.setLongestStreak(5);

        store.put(h1.getId(), h1);
        store.put(h2.getId(), h2);
        store.put(h3.getId(), h3);
    }

    @Override
    public Habit save(Habit habit) {
        if (habit.getId() == null || habit.getId().isBlank()) {
            habit.setId(UUID.randomUUID().toString());
        }
        store.put(habit.getId(), habit);
        return habit;
    }

    @Override
    public Optional<Habit> findById(String id) {
        return Optional.ofNullable(store.get(id));
    }

    @Override
    public List<Habit> findByUserId(String userId) {
        return store.values().stream()
                .filter(h -> h.getUserId().equals(userId))
                .collect(Collectors.toList());
    }

    @Override
    public List<Habit> findByUserIdAndTimeOfDay(String userId, String timeOfDay) {
        return store.values().stream()
                .filter(h -> h.getUserId().equals(userId) && h.getTimeOfDay().equalsIgnoreCase(timeOfDay))
                .collect(Collectors.toList());
    }

    @Override
    public void deleteById(String id) {
        store.remove(id);
    }

    @Override
    public List<Habit> findAll() {
        return new ArrayList<>(store.values());
    }
}