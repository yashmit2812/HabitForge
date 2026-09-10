import React from 'react';

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