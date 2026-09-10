import React, { useState, useEffect } from 'react';
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