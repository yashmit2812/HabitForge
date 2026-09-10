/**
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