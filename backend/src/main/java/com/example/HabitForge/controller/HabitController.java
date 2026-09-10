package com.example.HabitForge.controller;

import com.example.HabitForge.dto.HabitRequestDto;
import com.example.HabitForge.dto.HabitResponseDto;
import com.example.HabitForge.service.HabitService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * Habit Management REST Controller.
 *
 * Design Principle - Modularity and Separation of Concerns:
 * Purely responsible for HTTP endpoint binding, serialization, and status codes.
 * Delegates all domain logic to HabitService.
 */
@RestController
@RequestMapping("/api/habits")
@CrossOrigin(origins = "*")
public class HabitController {

    private final HabitService habitService;

    @Autowired
    public HabitController(HabitService habitService) {
        this.habitService = habitService;
    }

    @GetMapping
    public ResponseEntity<List<HabitResponseDto>> getHabits(
            @RequestParam(defaultValue = "user-default") String userId,
            @RequestParam(required = false) String timeOfDay) {
        if (timeOfDay != null && !timeOfDay.isBlank()) {
            return ResponseEntity.ok(habitService.getUserHabitsByTimeOfDay(userId, timeOfDay));
        }
        return ResponseEntity.ok(habitService.getUserHabits(userId));
    }

    @GetMapping("/{id}")
    public ResponseEntity<HabitResponseDto> getHabitById(@PathVariable String id) {
        return ResponseEntity.ok(habitService.getHabitById(id));
    }

    @PostMapping
    public ResponseEntity<HabitResponseDto> createHabit(
            @RequestParam(defaultValue = "user-default") String userId,
            @RequestBody HabitRequestDto request) {
        HabitResponseDto created = habitService.createHabit(userId, request);
        return new ResponseEntity<>(created, HttpStatus.CREATED);
    }

    @PostMapping("/{id}/complete")
    public ResponseEntity<HabitResponseDto> completeHabit(
            @PathVariable String id,
            @RequestParam(defaultValue = "user-default") String userId) {
        return ResponseEntity.ok(habitService.completeHabit(id, userId));
    }

    @PutMapping("/{id}")
    public ResponseEntity<HabitResponseDto> updateHabit(
            @PathVariable String id,
            @RequestBody HabitRequestDto request) {
        return ResponseEntity.ok(habitService.updateHabit(id, request));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteHabit(@PathVariable String id) {
        habitService.deleteHabit(id);
        return ResponseEntity.noContent().build();
    }
}