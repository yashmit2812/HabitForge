# HabitForge - UI/UX Design System & Figma Prototype Specification

**Project:** HabitForge (Gamified Habit Tracker)  
**Author:** Yashmit Sharma (Reg. No.: 24BAI1348)  
**Course:** Software Engineering (DA-2 / Review 2)  
**Design Tool:** Figma (Free Starter Plan)  
**Interactive Prototype Link:** [HabitForge Figma Prototype](https://www.figma.com/proto/habitforge-v2-system-design)

---

## 1. Design System & Tokens

### Color Palette (Dark Theme / Gamified RPG)
- **Background Primary:** `#090D16` (Deep Obsidian Void)
- **Background Secondary / Cards:** `#1E293B` (Slate 800)
- **Card Border Active:** `#38BDF8` (Sky Blue 400 - Quest Active)
- **Card Border Completed:** `#22C55E` (Emerald 500 - Quest Done)
- **Health Points (HP / Danger):** `#EF4444` (Loss Aversion Crimson)
- **Experience Points (XP / Reward):** `#F59E0B` (Dopamine Amber/Gold)
- **Typography Primary:** `#F8FAFC` (Slate 50)
- **Typography Muted:** `#94A3B8` (Slate 400)

### Typography Hierarchy
- **Font Family:** Inter / Plus Jakarta Sans (Modern Geometric Sans-Serif)
- **App Bar / Headers:** Bold 20px / 16px
- **Card Titles:** Bold 14px
- **Body & Subtitles:** Regular / Medium 12px
- **Badge & Pill Labels:** Bold 10px Uppercase

---

## 2. Six Core Screen Specifications

### Screen 1: Daily Quest Board (`screen1_quest_board.png`)
- **Purpose:** Primary daily execution hub where users view, filter, and check off habits.
- **Hero Stats Widget:** Shows real-time Health Points (85/100 HP) and Experience Points (340/500 XP) with animated gauge fills.
- **Visual Grouping:** Habits are grouped by Morning, Afternoon, and Evening to lower cognitive load.
- **Action:** One-click check-off button triggering instant visual state change (card turns emerald green, XP rises).

### Screen 2: Quest Creator & Difficulty Tuning Modal (`screen2_create_habit.png`)
- **Purpose:** Modal enabling users to configure new habits with gamified stakes.
- **Features:**
  - Dynamic XP reward and HP penalty scaling based on 4 difficulty tiers: Easy, Medium, Hard, Boss.
  - Category classification (Mindfulness, Study, Fitness, Creative).
  - Recurrence day selector (Monday through Sunday).

### Screen 3: Hero Profile & RPG Attributes (`screen3_hero_profile.png`)
- **Purpose:** Visual character sheet mapping personal consistency to RPG character stats.
- **Features:**
  - Avatar portrait, character title ("Routine Knight"), player level badge.
  - Discipline attributes (Intellect, Endurance, Mindfulness, Consistency).
  - Milestone achievement badges (7-Day Spark, Iron Body, Code Crusher).

### Screen 4: Streak Analytics & Consistency Heatmap (`screen4_analytics_heatmap.png`)
- **Purpose:** Validates user consistency through data visualization.
- **Features:**
  - GitHub-style 52-week consistency calendar heatmap.
  - Monthly completion rate comparison bar chart.
  - Key performance indicators: Current Streak, Longest Streak, Average Completion Rate.

### Screen 5: The Guild Shop / Custom Reward Bazaar (`screen5_reward_shop.png`)
- **Purpose:** Self-curated reward marketplace connecting virtual game coins with real-world guilt-free rewards.
- **Features:**
  - User gold balance display.
  - Reward cards with clear price tags (e.g., "1 Hour Gaming Session: 40 Gold").
  - Instant redemption button with affordability state verification.

### Screen 6: Adventurer's Guild & Social Feed (`screen6_guild_social.png`)
- **Purpose:** Social accountability feed leveraging peer support and collective goals.
- **Features:**
  - Weekly Party Boss Raid ("The Procrastination Dragon") where completed member habits deal collective boss damage.
  - Real-time activity feed showing friends' quest completions.
  - Cheer reaction button granting bonus XP to friends.

---

## 3. UI/UX Ergonomics & Heuristic Analysis

1. **Fitts's Law Compliance:**
   - Action buttons (e.g., "Complete Quest") are placed on the right-hand edge with ample touch targets (minimum 44x44px equivalent), making one-handed mobile and desktop interaction effortless.
2. **Cognitive Load Minimization:**
   - Instead of an overwhelming single list of 20 habits, quests are chunked into 3 distinct time horizons (Morning, Afternoon, Evening) using clean pill filters.
3. **Behavioral Psychology & Gamification Loops:**
   - **Loss Aversion:** The crimson HP bar introduces meaningful consequences—failing habits threatens player survival.
   - **Instant Dopamine:** Completing a habit immediately fills the amber XP gauge and awards spendable Gold coins.
4. **Accessibility (WCAG 2.1 AA Compliance):**
   - High color contrast ratio (minimum 7:1) for body text against dark backgrounds.
   - Color is never used as the sole indicator of status; icons, text badges, and strikethroughs reinforce state.
