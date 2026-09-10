import os
from pathlib import Path

front_base = Path(r"C:\Yashmit\SE PROJECT\frontend\src")

frontend_files = {
    front_base / "services" / "habitService.js": """/**
 * HabitForge REST API Client Service.
 *
 * Design Principle - Abstraction & Loose Coupling:
 * Shields UI components from raw Axios/Fetch HTTP requests, endpoints, and error handling.
 * If backend endpoints or schemas change, only this service file needs modification.
 */
const API_BASE = '/api';

export const habitService = {
  async getHabits(userId = 'user-default', timeOfDay = null) {
    const url = timeOfDay 
      ? `${API_BASE}/habits?userId=${userId}&timeOfDay=${timeOfDay}` 
      : `${API_BASE}/habits?userId=${userId}`;
    const res = await fetch(url);
    if (!res.ok) throw new Error('Failed to fetch habits');
    return res.json();
  },

  async createHabit(habitData, userId = 'user-default') {
    const res = await fetch(`${API_BASE}/habits?userId=${userId}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(habitData)
    });
    if (!res.ok) throw new Error('Failed to create habit');
    return res.json();
  },

  async completeHabit(habitId, userId = 'user-default') {
    const res = await fetch(`${API_BASE}/habits/${habitId}/complete?userId=${userId}`, {
      method: 'POST'
    });
    if (!res.ok) throw new Error('Failed to complete habit');
    return res.json();
  },

  async deleteHabit(habitId) {
    const res = await fetch(`${API_BASE}/habits/${habitId}`, {
      method: 'DELETE'
    });
    if (!res.ok) throw new Error('Failed to delete habit');
    return true;
  },

  async getPlayerStats(userId = 'user-default') {
    const res = await fetch(`${API_BASE}/gamification/stats?userId=${userId}`);
    if (!res.ok) throw new Error('Failed to fetch player stats');
    return res.json();
  }
};
""",

    front_base / "components" / "HeroStats.jsx": """import React from 'react';

/**
 * HeroStats Component.
 * Displays player level, avatar, HP (loss aversion) and XP progression bars.
 *
 * Design Principle - Modularity & High Cohesion:
 * Encapsulates purely player RPG presentation logic.
 */
export const HeroStats = ({ stats }) => {
  if (!stats) return null;

  return (
    <div className="hero-stats-card">
      <div className="hero-profile-summary">
        <div className="avatar-frame">
          <span className="avatar-icon">⚔️</span>
          <span className="level-badge">Lvl {stats.level}</span>
        </div>
        <div className="hero-title-group">
          <h2 className="hero-username">{stats.username}</h2>
          <span className="hero-class-tag">Novice Paladin • Streak Master</span>
        </div>
        <div className="gold-counter">
          🪙 <span className="gold-amount">{stats.gold} Gold</span>
        </div>
      </div>

      <div className="gauges-container">
        {/* Health Gauge (Loss Aversion) */}
        <div className="gauge-group">
          <div className="gauge-labels">
            <span className="gauge-name text-hp">❤️ Health Points (HP)</span>
            <span className="gauge-val">{stats.currentHp} / {stats.maxHp} HP</span>
          </div>
          <div className="progress-track hp-track">
            <div 
              className="progress-fill hp-fill" 
              style={{ width: `${stats.hpPercentage}%` }}
            />
          </div>
        </div>

        {/* XP Gauge (Dopamine Loop) */}
        <div className="gauge-group">
          <div className="gauge-labels">
            <span className="gauge-name text-xp">⭐ Experience Points (XP)</span>
            <span className="gauge-val">{stats.currentXp} / {stats.xpToNextLevel} XP</span>
          </div>
          <div className="progress-track xp-track">
            <div 
              className="progress-fill xp-fill" 
              style={{ width: `${stats.xpPercentage}%` }}
            />
          </div>
        </div>
      </div>
    </div>
  );
};
""",

    front_base / "components" / "HabitCard.jsx": """import React from 'react';

/**
 * HabitCard Component.
 * Represents an individual quest on the daily board.
 *
 * Design Principle - High Cohesion & Loose Coupling:
 * Handles visual state and triggers callback upon user check-off.
 */
export const HabitCard = ({ habit, onComplete, onDelete }) => {
  return (
    <div className={`habit-card ${habit.completedToday ? 'completed' : ''}`}>
      <div className="habit-info">
        <div className="habit-header-row">
          <span className={`category-pill category-${habit.category.toLowerCase()}`}>
            {habit.category}
          </span>
          <span className="time-badge">🕒 {habit.timeOfDay}</span>
          <span className="streak-badge">
            🔥 {habit.currentStreak} {habit.currentStreak === 1 ? 'day' : 'days'}
          </span>
        </div>
        <h3 className="habit-title">{habit.title}</h3>
        <p className="habit-desc">{habit.description}</p>
        <div className="habit-rewards-row">
          <span className="reward-tag text-xp">+{habit.xpReward} XP</span>
          <span className="penalty-tag text-hp">-{habit.hpPenalty} HP on fail</span>
        </div>
      </div>

      <div className="habit-actions">
        <button
          className={`btn-checkin ${habit.completedToday ? 'btn-done' : 'btn-active'}`}
          onClick={() => !habit.completedToday && onComplete(habit.id)}
          disabled={habit.completedToday}
        >
          {habit.completedToday ? '✓ Quest Done' : 'Complete Quest'}
        </button>
      </div>
    </div>
  );
};
""",

    front_base / "components" / "QuestBoard.jsx": """import React, { useState, useEffect } from 'react';
import { HeroStats } from './HeroStats';
import { HabitCard } from './HabitCard';
import { habitService } from '../services/habitService';

/**
 * QuestBoard Component.
 * Main hub containing player summary, filter tabs, and active habit quests.
 */
export const QuestBoard = () => {
  const [habits, setHabits] = useState([]);
  const [stats, setStats] = useState(null);
  const [activeFilter, setActiveFilter] = useState('All');
  const [loading, setLoading] = useState(true);

  const loadData = async () => {
    try {
      setLoading(true);
      const [fetchedHabits, fetchedStats] = await Promise.all([
        habitService.getHabits(),
        habitService.getPlayerStats()
      ]);
      setHabits(fetchedHabits);
      setStats(fetchedStats);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadData();
  }, []);

  const handleComplete = async (habitId) => {
    try {
      await habitService.completeHabit(habitId);
      await loadData();
    } catch (err) {
      console.error('Failed to complete habit', err);
    }
  };

  const filteredHabits = activeFilter === 'All'
    ? habits
    : habits.filter(h => h.timeOfDay.toLowerCase() === activeFilter.toLowerCase());

  return (
    <div className="quest-board-layout">
      <HeroStats stats={stats} />

      <div className="quest-board-header">
        <div className="board-title-group">
          <h2>Daily Quest Log</h2>
          <p className="subtitle">Clear your daily commitments before midnight to protect your HP!</p>
        </div>
        <div className="filter-pills">
          {['All', 'Morning', 'Afternoon', 'Evening'].map((filter) => (
            <button
              key={filter}
              className={`pill-btn ${activeFilter === filter ? 'active' : ''}`}
              onClick={() => setActiveFilter(filter)}
            >
              {filter}
            </button>
          ))}
        </div>
      </div>

      <div className="quests-grid">
        {loading ? (
          <p>Loading quests from server...</p>
        ) : filteredHabits.length > 0 ? (
          filteredHabits.map((habit) => (
            <HabitCard
              key={habit.id}
              habit={habit}
              onComplete={handleComplete}
            />
          ))
        ) : (
          <p className="empty-state">No quests active for this filter.</p>
        )}
      </div>
    </div>
  );
};
"""
}

for path, content in frontend_files.items():
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip(), encoding="utf-8")
    print(f"Created frontend component: {path.name}")

print("Frontend components successfully generated!")
