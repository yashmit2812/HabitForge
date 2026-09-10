package com.example.HabitForge.controller;

import com.example.HabitForge.dto.UserStatsDto;
import com.example.HabitForge.service.GamificationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

/**
 * Gamification and Character Stats REST Controller.
 */
@RestController
@RequestMapping("/api/gamification")
@CrossOrigin(origins = "*")
public class GamificationController {

    private final GamificationService gamificationService;

    @Autowired
    public GamificationController(GamificationService gamificationService) {
        this.gamificationService = gamificationService;
    }

    @GetMapping("/stats")
    public ResponseEntity<UserStatsDto> getUserStats(
            @RequestParam(defaultValue = "user-default") String userId) {
        return ResponseEntity.ok(gamificationService.getUserStats(userId));
    }

    @PostMapping("/damage")
    public ResponseEntity<UserStatsDto> applyPenalty(
            @RequestParam(defaultValue = "user-default") String userId,
            @RequestParam(defaultValue = "15") int hpDamage) {
        return ResponseEntity.ok(gamificationService.deductHpPenalty(userId, hpDamage));
    }
}