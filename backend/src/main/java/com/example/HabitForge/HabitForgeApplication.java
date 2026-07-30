package com.example.HabitForge;

import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class HabitForgeApplication {

	public static void main(String[] args) {
		SpringApplication.run(HabitForgeApplication.class, args);
	}

	@Bean
	CommandLineRunner test() {
		return args -> System.out.println("Application Started Successfully");
	}
}