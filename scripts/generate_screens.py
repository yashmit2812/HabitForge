import os
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

screens_dir = Path(r"C:\Yashmit\SE PROJECT\docs\design\screens")
screens_dir.mkdir(parents=True, exist_ok=True)

# Helper function to style UI cards
def base_screen(title_bar_text):
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=200)
    fig.patch.set_facecolor("#090d16")
    ax.set_facecolor("#090d16")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    # App Nav Bar
    navbar = patches.FancyBboxPatch((2, 91), 96, 7, boxstyle="square,pad=0",
                                   facecolor="#111827", edgecolor="#1f2937", linewidth=1.5)
    ax.add_patch(navbar)
    ax.text(5, 94.5, "[H] HabitForge", color="#38bdf8", fontsize=13, fontweight="bold", va="center")
    
    # Nav items
    navs = ["Quests", "Profile", "Analytics", "Bazaar", "Guild"]
    for idx, item in enumerate(navs):
        color = "#38bdf8" if item in title_bar_text else "#94a3b8"
        fontweight = "bold" if item in title_bar_text else "normal"
        ax.text(26 + idx * 11, 94.5, item, color=color, fontsize=10, fontweight=fontweight, va="center")

    # Right profile pill
    ax.text(82, 94.5, "Lvl 4 Yashmit", color="#f8fafc", fontsize=9.5, fontweight="bold", va="center")
    ax.text(94, 94.5, "120 G", color="#fbbf24", fontsize=9.5, fontweight="bold", va="center")

    return fig, ax

# -------------------------------------------------------------
# Screen 1: Daily Quest Board
# -------------------------------------------------------------
fig1, ax1 = base_screen("Quests")

# Hero Stats Banner
banner = patches.FancyBboxPatch((4, 73), 92, 16, boxstyle="round,pad=0.5,rounding_size=1",
                               facecolor="#1e293b", edgecolor="#334155", linewidth=1.5)
ax1.add_patch(banner)
ax1.text(7, 84, "Yashmit The Disciplined", color="#f8fafc", fontsize=12, fontweight="bold")
ax1.text(7, 80, "Class: Paladin of Routine | Active Streak: 12 Days", color="#94a3b8", fontsize=9)

# HP Bar
ax1.text(7, 76.5, "Health Points (HP): 85 / 100", color="#f87171", fontsize=8.5, fontweight="bold")
hp_bg = patches.Rectangle((7, 74), 40, 1.8, facecolor="#334155", edgecolor="none")
hp_fg = patches.Rectangle((7, 74), 34, 1.8, facecolor="#ef4444", edgecolor="none")
ax1.add_patch(hp_bg)
ax1.add_patch(hp_fg)

# XP Bar
ax1.text(52, 76.5, "Experience (XP): 340 / 500 (Level 4)", color="#fbbf24", fontsize=8.5, fontweight="bold")
xp_bg = patches.Rectangle((52, 74), 40, 1.8, facecolor="#334155", edgecolor="none")
xp_fg = patches.Rectangle((52, 74), 27.2, 1.8, facecolor="#f59e0b", edgecolor="none")
ax1.add_patch(xp_bg)
ax1.add_patch(xp_fg)

# Quests Header
ax1.text(4, 68.5, "Daily Quest Board", color="#f8fafc", fontsize=13, fontweight="bold")
ax1.text(4, 65.5, "Complete tasks before midnight to defend your HP pool", color="#64748b", fontsize=8.5)

# Filter pills
pills = ["All (3)", "Morning (1)", "Afternoon (1)", "Evening (1)"]
for i, p in enumerate(pills):
    p_box = patches.FancyBboxPatch((60 + i*9.5, 66), 8.5, 3.5, boxstyle="round,pad=0.2,rounding_size=0.8",
                                  facecolor="#0284c7" if i==0 else "#1e293b", edgecolor="#38bdf8" if i==0 else "#334155")
    ax1.add_patch(p_box)
    ax1.text(60 + i*9.5 + 4.25, 67.7, p, color="#ffffff" if i==0 else "#94a3b8", fontsize=7.5, ha="center", va="center")

# Quest Cards
quests = [
    ("Morning Meditation & Mindfulness", "15 mins breathwork before screens", "Morning", "+20 XP", "-10 HP", "5 Days", True),
    ("Code 1 Algorithmic Problem", "Solve 1 Medium LeetCode / Data Structure problem", "Afternoon", "+35 XP", "-20 HP", "12 Days", False),
    ("Evening Strength Workout", "45 min calisthenics or barbell training", "Evening", "+30 XP", "-15 HP", "3 Days", False)
]

for idx, (title, desc, tod, xp, hp, streak, done) in enumerate(quests):
    y = 48 - idx * 16
    q_card = patches.FancyBboxPatch((4, y), 92, 13.5, boxstyle="round,pad=0.5,rounding_size=1",
                                   facecolor="#162032" if not done else "#14251f",
                                   edgecolor="#3b82f6" if not done else "#22c55e", linewidth=1.5)
    ax1.add_patch(q_card)
    
    # Text
    ax1.text(7, y + 9.5, title, color="#f8fafc", fontsize=11, fontweight="bold")
    ax1.text(7, y + 6.2, desc, color="#94a3b8", fontsize=8.5)
    
    # Badges
    ax1.text(7, y + 2.5, f"[{tod}]  Streak: {streak}  |  Reward: {xp}  |  Risk: {hp}",
             color="#38bdf8" if not done else "#4ade80", fontsize=8)

    # Action button
    btn = patches.FancyBboxPatch((78, y + 3.5), 15, 6.5, boxstyle="round,pad=0.2,rounding_size=0.8",
                                facecolor="#22c55e" if done else "#2563eb", edgecolor="none")
    ax1.add_patch(btn)
    ax1.text(85.5, y + 6.75, "Done" if done else "Complete Quest",
             color="#ffffff", fontsize=8, fontweight="bold", ha="center", va="center")

plt.savefig(screens_dir / "screen1_quest_board.png", facecolor=fig1.get_facecolor(), edgecolor="none")
plt.close()
print("Saved screen1_quest_board.png")

# -------------------------------------------------------------
# Screen 2: Create / Edit Quest Modal
# -------------------------------------------------------------
fig2, ax2 = base_screen("Quests")

# Dim background
dim = patches.Rectangle((0, 0), 100, 100, facecolor="#000000", alpha=0.6)
ax2.add_patch(dim)

# Modal Box
modal = patches.FancyBboxPatch((15, 12), 70, 75, boxstyle="round,pad=0.8,rounding_size=1.5",
                              facecolor="#0f172a", edgecolor="#38bdf8", linewidth=2)
ax2.add_patch(modal)

ax2.text(19, 81, "Forge New Daily Quest", color="#f8fafc", fontsize=14, fontweight="bold")
ax2.text(19, 78, "Configure your objective, time window, and gamified stakes", color="#94a3b8", fontsize=8.5)

# Inputs
ax2.text(19, 73, "Quest Title", color="#cbd5e1", fontsize=9, fontweight="bold")
f1 = patches.FancyBboxPatch((19, 67), 62, 4.5, boxstyle="round,pad=0.2", facecolor="#1e293b", edgecolor="#475569")
ax2.add_patch(f1)
ax2.text(21, 69.2, "Read 20 Pages of System Design Architecture", color="#f8fafc", fontsize=9)

ax2.text(19, 63, "Description / Objectives", color="#cbd5e1", fontsize=9, fontweight="bold")
f2 = patches.FancyBboxPatch((19, 53), 62, 8, boxstyle="round,pad=0.2", facecolor="#1e293b", edgecolor="#475569")
ax2.add_patch(f2)
ax2.text(21, 58, "Study Chapter 4: Distributed Caching & Event-Driven Patterns", color="#94a3b8", fontsize=8.5)

# Category & Time of Day
ax2.text(19, 49, "Category", color="#cbd5e1", fontsize=9, fontweight="bold")
c1 = patches.FancyBboxPatch((19, 43), 28, 4.5, boxstyle="round,pad=0.2", facecolor="#1e293b", edgecolor="#475569")
ax2.add_patch(c1)
ax2.text(22, 45.2, "Study & Academics v", color="#f8fafc", fontsize=8.5)

ax2.text(53, 49, "Time of Day", color="#cbd5e1", fontsize=9, fontweight="bold")
c2 = patches.FancyBboxPatch((53, 43), 28, 4.5, boxstyle="round,pad=0.2", facecolor="#1e293b", edgecolor="#475569")
ax2.add_patch(c2)
ax2.text(56, 45.2, "Morning [6 AM - 12 PM] v", color="#f8fafc", fontsize=8.5)

# Difficulty & Stakes
ax2.text(19, 39, "Quest Difficulty & Gamified Stakes", color="#cbd5e1", fontsize=9, fontweight="bold")
diffs = [("Easy", "+10 XP", "-5 HP"), ("Medium", "+25 XP", "-15 HP"), ("Hard", "+45 XP", "-30 HP"), ("Boss", "+80 XP", "-50 HP")]
for i, (name, xp, hp) in enumerate(diffs):
    d_box = patches.FancyBboxPatch((19 + i*16, 29), 14, 8, boxstyle="round,pad=0.2",
                                  facecolor="#0284c7" if i==1 else "#1e293b",
                                  edgecolor="#38bdf8" if i==1 else "#334155", linewidth=1.5)
    ax2.add_patch(d_box)
    ax2.text(19 + i*16 + 7, 34.5, name, color="#ffffff", fontsize=9, fontweight="bold", ha="center")
    ax2.text(19 + i*16 + 7, 31, f"{xp} / {hp}", color="#cbd5e1" if i!=1 else "#e0f2fe", fontsize=7.5, ha="center")

# Buttons
btn_cancel = patches.FancyBboxPatch((47, 18), 16, 5.5, boxstyle="round,pad=0.2", facecolor="#334155", edgecolor="none")
btn_save = patches.FancyBboxPatch((65, 18), 16, 5.5, boxstyle="round,pad=0.2", facecolor="#2563eb", edgecolor="none")
ax2.add_patch(btn_cancel)
ax2.add_patch(btn_save)
ax2.text(55, 20.7, "Cancel", color="#cbd5e1", fontsize=8.5, ha="center")
ax2.text(73, 20.7, "Forge Quest", color="#ffffff", fontsize=8.5, fontweight="bold", ha="center")

plt.savefig(screens_dir / "screen2_create_habit.png", facecolor=fig2.get_facecolor(), edgecolor="none")
plt.close()
print("Saved screen2_create_habit.png")

# -------------------------------------------------------------
# Screen 3: Hero Profile & RPG Attributes
# -------------------------------------------------------------
fig3, ax3 = base_screen("Profile")

# Left Column: Avatar & Vitals
col1 = patches.FancyBboxPatch((4, 8), 36, 80, boxstyle="round,pad=0.5,rounding_size=1",
                             facecolor="#1e293b", edgecolor="#334155")
ax3.add_patch(col1)

# Avatar circle placeholder
avatar = patches.Circle((22, 70), 10, facecolor="#0284c7", edgecolor="#38bdf8", linewidth=2)
ax3.add_patch(avatar)
ax3.text(22, 70, "PALADIN", color="#ffffff", fontsize=8.5, fontweight="bold", ha="center", va="center")

ax3.text(22, 56, "Yashmit Sharma", color="#f8fafc", fontsize=13, fontweight="bold", ha="center")
ax3.text(22, 52, "Level 4 Routine Knight", color="#38bdf8", fontsize=9.5, ha="center")
ax3.text(22, 48, "Title: The Early Riser", color="#fbbf24", fontsize=8.5, ha="center")

# Stats details
stats_text = [
    ("Max Health:", "100 HP"),
    ("Current XP:", "340 / 500"),
    ("Bazaar Gold:", "120 Coins"),
    ("Active Streaks:", "3 Habits"),
    ("Consistency Score:", "94%")
]
for i, (k, v) in enumerate(stats_text):
    ax3.text(8, 41 - i*5, k, color="#94a3b8", fontsize=8.5)
    ax3.text(36, 41 - i*5, v, color="#f8fafc", fontsize=8.5, fontweight="bold", ha="right")

# Right Column: Attribute Radar & Unlocked Badges
col2 = patches.FancyBboxPatch((43, 49), 53, 39, boxstyle="round,pad=0.5,rounding_size=1",
                             facecolor="#1e293b", edgecolor="#334155")
ax3.add_patch(col2)
ax3.text(46, 83, "Discipline Attributes", color="#f8fafc", fontsize=12, fontweight="bold")

attrs = [
    ("Intellect (Study & Code)", 82, "#38bdf8"),
    ("Endurance (Fitness & Gym)", 68, "#ef4444"),
    ("Mindfulness (Meditation)", 75, "#a855f7"),
    ("Consistency (Streak Purity)", 90, "#22c55e")
]
for i, (name, val, col) in enumerate(attrs):
    y = 75 - i * 6.5
    ax3.text(46, y + 2, f"{name}: {val}/100", color="#cbd5e1", fontsize=8)
    bg = patches.Rectangle((46, y), 47, 1.5, facecolor="#334155", edgecolor="none")
    fg = patches.Rectangle((46, y), 47 * (val/100.0), 1.5, facecolor=col, edgecolor="none")
    ax3.add_patch(bg)
    ax3.add_patch(fg)

# Badges Section
col3 = patches.FancyBboxPatch((43, 8), 53, 38, boxstyle="round,pad=0.5,rounding_size=1",
                             facecolor="#1e293b", edgecolor="#334155")
ax3.add_patch(col3)
ax3.text(46, 41, "Unlocked Milestone Badges", color="#f8fafc", fontsize=12, fontweight="bold")

badges = [
    ("7-Day Spark", "Completed 7 days uninterrupted", "#fbbf24"),
    ("Iron Body", "Completed 15 Fitness sessions", "#ef4444"),
    ("Code Crusher", "Solved 25 LeetCode quests", "#38bdf8"),
    ("Grandmaster", "Reach Level 10 (Locked)", "#64748b")
]
for i, (name, desc, col) in enumerate(badges):
    x = 46 + (i % 2) * 24
    y = 28 if i < 2 else 15
    b_card = patches.FancyBboxPatch((x, y), 22, 9.5, boxstyle="round,pad=0.2",
                                   facecolor="#0f172a", edgecolor=col, linewidth=1.2)
    ax3.add_patch(b_card)
    ax3.text(x + 2, y + 6.5, name, color=col, fontsize=8.5, fontweight="bold")
    ax3.text(x + 2, y + 2.5, desc, color="#94a3b8", fontsize=6.8)

plt.savefig(screens_dir / "screen3_hero_profile.png", facecolor=fig3.get_facecolor(), edgecolor="none")
plt.close()
print("Saved screen3_hero_profile.png")

# -------------------------------------------------------------
# Screen 4: Streak Analytics & Consistency Heatmap
# -------------------------------------------------------------
fig4, ax4 = base_screen("Analytics")

# Top KPI Summary Cards
kpis = [
    ("Current Streak", "12 Days", "#38bdf8"),
    ("Best Streak", "18 Days", "#a855f7"),
    ("Total XP Earned", "2,840 XP", "#fbbf24"),
    ("Avg Completion", "89.4%", "#22c55e")
]
for i, (label, val, col) in enumerate(kpis):
    x = 4 + i * 23.5
    k_card = patches.FancyBboxPatch((x, 72), 22, 16, boxstyle="round,pad=0.4,rounding_size=0.8",
                                   facecolor="#1e293b", edgecolor="#334155")
    ax4.add_patch(k_card)
    ax4.text(x + 11, 82, label, color="#94a3b8", fontsize=8.5, ha="center")
    ax4.text(x + 11, 75.5, val, color=col, fontsize=13, fontweight="bold", ha="center")

# Heatmap Box
hm_box = patches.FancyBboxPatch((4, 38), 92, 31, boxstyle="round,pad=0.5,rounding_size=1",
                               facecolor="#1e293b", edgecolor="#334155")
ax4.add_patch(hm_box)
ax4.text(7, 64, "Annual Habit Consistency Heatmap (Last 20 Weeks)", color="#f8fafc", fontsize=11, fontweight="bold")

# Draw simulated Github grid
np.random.seed(42)
colors = ["#1e293b", "#064e3b", "#047857", "#10b981", "#34d399"]
for w in range(26):
    for d in range(7):
        intensity = np.random.choice([1, 2, 3, 4], p=[0.15, 0.25, 0.35, 0.25])
        cell = patches.Rectangle((7 + w * 3.3, 41 + (6-d)*2.8), 2.7, 2.3,
                                 facecolor=colors[intensity], edgecolor="none")
        ax4.add_patch(cell)

# Monthly Progress Chart Box
chart_box = patches.FancyBboxPatch((4, 8), 92, 27, boxstyle="round,pad=0.5,rounding_size=1",
                                  facecolor="#1e293b", edgecolor="#334155")
ax4.add_patch(chart_box)
ax4.text(7, 30.5, "Monthly Habit Completion Rate vs HP Preserved", color="#f8fafc", fontsize=11, fontweight="bold")

months = ["May", "June", "July", "August", "September"]
rates = [72, 79, 85, 88, 93]
for i, (m, r) in enumerate(zip(months, rates)):
    bx = 14 + i * 16
    ax4.text(bx + 4, 11, m, color="#94a3b8", fontsize=8, ha="center")
    b_fg = patches.Rectangle((bx, 14), 8, r * 0.14, facecolor="#0284c7", edgecolor="#38bdf8")
    ax4.add_patch(b_fg)
    ax4.text(bx + 4, 15 + r*0.14, f"{r}%", color="#38bdf8", fontsize=7.5, fontweight="bold", ha="center")

plt.savefig(screens_dir / "screen4_analytics_heatmap.png", facecolor=fig4.get_facecolor(), edgecolor="none")
plt.close()
print("Saved screen4_analytics_heatmap.png")

# -------------------------------------------------------------
# Screen 5: The Guild Shop / Custom Reward Bazaar
# -------------------------------------------------------------
fig5, ax5 = base_screen("Bazaar")

# Shop Header
ax5.text(4, 85, "The Item Bazaar (Reward Shop)", color="#f8fafc", fontsize=14, fontweight="bold")
ax5.text(4, 82, "Spend your hard-earned habit gold on guilt-free real-world rewards", color="#94a3b8", fontsize=8.5)

# Gold counter badge
g_card = patches.FancyBboxPatch((72, 80), 24, 7.5, boxstyle="round,pad=0.2",
                               facecolor="#78350f", edgecolor="#f59e0b", linewidth=1.5)
ax5.add_patch(g_card)
ax5.text(84, 83.75, "Available: 120 Gold", color="#fef3c7", fontsize=9.5, fontweight="bold", ha="center", va="center")

# Shop Items
items = [
    ("1 Hour Video Gaming", "Guilt-free gaming session after study", "40 Gold", "#38bdf8", True),
    ("Specialty Coffee & Treat", "Artisan espresso from your favorite cafe", "60 Gold", "#f59e0b", True),
    ("Movie Theater Night", "Weekend IMAX film ticket + popcorn", "100 Gold", "#a855f7", True),
    ("Cheat Meal Feast", "Full restaurant cheat meal without guilt", "120 Gold", "#ef4444", True),
    ("New Mechanical Keyboard", "Tech gear reward milestone", "350 Gold", "#64748b", False),
    ("Weekend Getaway Trip", "Full weekend nature cabin retreat", "600 Gold", "#64748b", False)
]

for idx, (title, desc, cost, col, affordable) in enumerate(items):
    col_idx = idx % 3
    row_idx = idx // 3
    x = 4 + col_idx * 31.5
    y = 48 - row_idx * 30
    
    i_card = patches.FancyBboxPatch((x, y), 29.5, 26, boxstyle="round,pad=0.5,rounding_size=1",
                                   facecolor="#1e293b", edgecolor=col, linewidth=1.5)
    ax5.add_patch(i_card)
    
    ax5.text(x + 3, y + 21, title, color="#f8fafc", fontsize=9.5, fontweight="bold")
    ax5.text(x + 3, y + 14, desc, color="#94a3b8", fontsize=7.5)
    ax5.text(x + 3, y + 9, f"Cost: {cost}", color=col, fontsize=8.5, fontweight="bold")
    
    btn = patches.FancyBboxPatch((x + 3, y + 2.5), 23.5, 4.8, boxstyle="round,pad=0.2",
                                facecolor="#2563eb" if affordable else "#334155", edgecolor="none")
    ax5.add_patch(btn)
    ax5.text(x + 14.75, y + 4.9, "Redeem Reward" if affordable else "Need More Gold",
             color="#ffffff" if affordable else "#94a3b8", fontsize=7.5, fontweight="bold", ha="center", va="center")

plt.savefig(screens_dir / "screen5_reward_shop.png", facecolor=fig5.get_facecolor(), edgecolor="none")
plt.close()
print("Saved screen5_reward_shop.png")

# -------------------------------------------------------------
# Screen 6: Adventurer's Guild & Social Feed
# -------------------------------------------------------------
fig6, ax6 = base_screen("Guild")

# Boss Raid Banner
boss = patches.FancyBboxPatch((4, 70), 92, 18, boxstyle="round,pad=0.5,rounding_size=1",
                             facecolor="#450a0a", edgecolor="#ef4444", linewidth=2)
ax6.add_patch(boss)
ax6.text(7, 83.5, "Party Raid: The Procrastination Dragon", color="#fecaca", fontsize=12, fontweight="bold")
ax6.text(7, 79.5, "Party habits deal collective damage! Clear 50 habits this week to defeat the boss.", color="#fca5a5", fontsize=8)
ax6.text(7, 75.5, "Boss Health: 420 / 1000 HP", color="#ffffff", fontsize=8.5, fontweight="bold")

b_bg = patches.Rectangle((7, 72.5), 86, 2, facecolor="#7f1d1d", edgecolor="none")
b_fg = patches.Rectangle((7, 72.5), 36.1, 2, facecolor="#ef4444", edgecolor="none")
ax6.add_patch(b_bg)
ax6.add_patch(b_fg)

# Feed Header
ax6.text(4, 65, "Guild Activity Feed & Cheering", color="#f8fafc", fontsize=12, fontweight="bold")

# Feed Items
feed_events = [
    ("Jordan Chen", "Morning 5K Run", "+25 XP", "25m ago", "Dealt 15 damage to Boss!"),
    ("Aria Smith", "Deep Work Sprint (2h)", "+45 XP", "1h ago", "Dealt 25 damage to Boss!"),
    ("Yashmit Sharma", "Code 1 Algorithmic Problem", "+35 XP", "2h ago", "Dealt 20 damage to Boss!"),
    ("Dev Patel", "15min Guided Meditation", "+20 XP", "3h ago", "Dealt 10 damage to Boss!")
]

for idx, (user, quest, xp, time, impact) in enumerate(feed_events):
    y = 49 - idx * 13
    f_card = patches.FancyBboxPatch((4, y), 92, 11, boxstyle="round,pad=0.4,rounding_size=0.8",
                                   facecolor="#1e293b", edgecolor="#334155")
    ax6.add_patch(f_card)
    
    ax6.text(7, y + 7, f"{user} completed '{quest}' ({xp})", color="#f8fafc", fontsize=9.5, fontweight="bold")
    ax6.text(7, y + 3, f"{impact}  •  {time}", color="#38bdf8", fontsize=8)
    
    cheer_btn = patches.FancyBboxPatch((76, y + 2.5), 17, 5.5, boxstyle="round,pad=0.2",
                                      facecolor="#065f46", edgecolor="#10b981")
    ax6.add_patch(cheer_btn)
    ax6.text(84.5, y + 5.25, "Cheer (+5 XP)", color="#a7f3d0", fontsize=7.5, fontweight="bold", ha="center", va="center")

plt.savefig(screens_dir / "screen6_guild_social.png", facecolor=fig6.get_facecolor(), edgecolor="none")
plt.close()
print("Saved screen6_guild_social.png")

print("All 6 Figma screen mocks generated successfully!")
