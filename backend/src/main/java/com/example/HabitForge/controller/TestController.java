package com.example.HabitForge.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api")
public class TestController {

    @GetMapping("/status")
    public String checkStatus() {
        return "HabitForge Spring Boot Backend is running successfully!";
    }
}