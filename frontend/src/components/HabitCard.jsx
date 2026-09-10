import React from 'react';

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