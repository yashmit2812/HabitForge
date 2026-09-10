import os
import xml.etree.ElementTree as ET
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches

output_dir = Path(r"C:\Yashmit\SE PROJECT\docs\design")
output_dir.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------------
# 1. High-Level Architecture Diagram (.drawio and .png)
# -------------------------------------------------------------
drawio_arch_xml = """<mxfile host="app.diagrams.net" modified="2026-09-10T18:00:00.000Z" agent="HabitForge Design" version="24.7.5">
  <diagram id="arch-diag" name="HabitForge High-Level Architecture">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1200" pageHeight="800" background="#0f172a" math="0" shadow="1">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Docker Container Boundary -->
        <mxCell id="box_docker" value="Docker Compose Orchestration Environment (Network: seproject_default)" style="rounded=1;whiteSpace=wrap;html=1;dashed=1;strokeColor=#38bdf8;strokeWidth=2;fillColor=#1e293b;fontColor=#94a3b8;verticalAlign=top;align=left;spacingLeft=15;spacingTop=10;fontStyle=1;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="1120" height="720" as="geometry"/>
        </mxCell>

        <!-- Presentation Tier -->
        <mxCell id="box_client" value="Client / Presentation Tier&#xa;React 18 + Vite (Port: 5173)" style="rounded=1;whiteSpace=wrap;html=1;strokeColor=#0284c7;strokeWidth=2;fillColor=#0369a1;fontColor=#ffffff;verticalAlign=top;align=center;spacingTop=10;fontStyle=1;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="80" y="100" width="280" height="600" as="geometry"/>
        </mxCell>
        <mxCell id="c_ui_comp" value="Modular UI Components&#xa;• QuestBoard.jsx&#xa;• HeroStats.jsx (HP/XP)&#xa;• HabitCard.jsx&#xa;• CreateQuestModal.jsx&#xa;• AnalyticsHeatmap.jsx&#xa;• RewardShop.jsx" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#0c4a6e;strokeColor=#38bdf8;fontColor=#f0f9ff;fontSize=12;align=left;spacingLeft=10;" vertex="1" parent="1">
          <mxGeometry x="100" y="170" width="240" height="150" as="geometry"/>
        </mxCell>
        <mxCell id="c_state" value="Client State &amp; Cache&#xa;• React Hooks (useState, useEffect)&#xa;• Optimistic UI Updates&#xa;• Local Theme Preference" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#0c4a6e;strokeColor=#38bdf8;fontColor=#f0f9ff;fontSize=12;align=left;spacingLeft=10;" vertex="1" parent="1">
          <mxGeometry x="100" y="340" width="240" height="110" as="geometry"/>
        </mxCell>
        <mxCell id="c_api_service" value="API Client Layer&#xa;• habitService.js&#xa;• Abstracted HTTP (Fetch/Axios)&#xa;• JWT Auth Token Interceptor" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#0c4a6e;strokeColor=#38bdf8;fontColor=#f0f9ff;fontSize=12;align=left;spacingLeft=10;" vertex="1" parent="1">
          <mxGeometry x="100" y="470" width="240" height="110" as="geometry"/>
        </mxCell>

        <!-- REST API Bridge -->
        <mxCell id="conn_rest" value="HTTPS / JSON&#xa;REST API calls&#xa;(Port 8080)" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#38bdf8;strokeWidth=3;fontColor=#38bdf8;fontSize=12;fontStyle=1;" edge="1" parent="1" source="c_api_service" target="box_server">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- Application Tier -->
        <mxCell id="box_server" value="Application Tier (Server)&#xa;Spring Boot REST API (Port: 8080)" style="rounded=1;whiteSpace=wrap;html=1;strokeColor=#16a34a;strokeWidth=2;fillColor=#15803d;fontColor=#ffffff;verticalAlign=top;align=center;spacingTop=10;fontStyle=1;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="460" y="100" width="360" height="600" as="geometry"/>
        </mxCell>
        <mxCell id="s_ctrl" value="REST Controllers&#xa;• HabitController (/api/habits)&#xa;• GamificationController (/api/gamification)&#xa;• AuthController (/api/auth)&#xa;• HealthCheck (/api/status)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#14532d;strokeColor=#4ade80;fontColor=#f0fdf4;fontSize=12;align=left;spacingLeft=10;" vertex="1" parent="1">
          <mxGeometry x="480" y="160" width="320" height="110" as="geometry"/>
        </mxCell>
        <mxCell id="s_service" value="Business Logic &amp; Domain Services&#xa;• HabitServiceImpl (implements HabitService)&#xa;• GamificationService (HP/XP/Levels)&#xa;• StreakCalculationService (Cohesion)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#14532d;strokeColor=#4ade80;fontColor=#f0fdf4;fontSize=12;align=left;spacingLeft=10;" vertex="1" parent="1">
          <mxGeometry x="480" y="290" width="320" height="120" as="geometry"/>
        </mxCell>
        <mxCell id="s_strategy" value="Strategy Pattern &amp; Schedulers&#xa;• StreakStrategy (DailyStreakStrategy)&#xa;• Midnight Cron Job (@Scheduled)&#xa;• DTO Mappers &amp; Validation" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#14532d;strokeColor=#4ade80;fontColor=#f0fdf4;fontSize=12;align=left;spacingLeft=10;" vertex="1" parent="1">
          <mxGeometry x="480" y="430" width="320" height="110" as="geometry"/>
        </mxCell>
        <mxCell id="s_repo" value="Data Repositories (Abstraction)&#xa;• HabitRepository Interface&#xa;• UserRepository Interface&#xa;• Spring Data MongoDB" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#14532d;strokeColor=#4ade80;fontColor=#f0fdf4;fontSize=12;align=left;spacingLeft=10;" vertex="1" parent="1">
          <mxGeometry x="480" y="560" width="320" height="110" as="geometry"/>
        </mxCell>

        <!-- Database Bridge -->
        <mxCell id="conn_db" value="TCP / Spring Data&#xa;Mongo Driver&#xa;(Port 27017)" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#4ade80;strokeWidth=3;fontColor=#4ade80;fontSize=12;fontStyle=1;" edge="1" parent="1" source="s_repo" target="box_db">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

        <!-- Data Persistence Tier -->
        <mxCell id="box_db" value="Data Persistence Tier&#xa;MongoDB Document Database (Port: 27017)" style="rounded=1;whiteSpace=wrap;html=1;strokeColor=#d97706;strokeWidth=2;fillColor=#b45309;fontColor=#ffffff;verticalAlign=top;align=center;spacingTop=10;fontStyle=1;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="900" y="100" width="220" height="600" as="geometry"/>
        </mxCell>
        <mxCell id="db_colls" value="NoSQL Collections&#xa;&#xa;• habits&#xa;• quest title, frequency, time&#xa;• current_streak, longest_streak&#xa;• xp_reward, hp_penalty&#xa;&#xa;• users&#xa;• credentials, profile avatar&#xa;• current_hp, max_hp, xp&#xa;• level, gold, unlocked_badges&#xa;&#xa;• daily_logs&#xa;• timestamps &amp; check-in history" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#78350f;strokeColor=#f59e0b;fontColor=#fef3c7;fontSize=12;align=left;spacingLeft=15;" vertex="1" parent="1">
          <mxGeometry x="920" y="180" width="180" height="490" as="geometry"/>
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
"""

(output_dir / "habitforge_architecture.drawio").write_text(drawio_arch_xml.strip(), encoding="utf-8")
print("Saved habitforge_architecture.drawio")

# Render High-Res PNG for Architecture Diagram using Matplotlib
fig, ax = plt.subplots(figsize=(15, 9), dpi=200)
ax.set_facecolor("#0f172a")
fig.patch.set_facecolor("#0f172a")

# Title
ax.text(0.5, 0.96, "HabitForge: High-Level Layered System Architecture",
        transform=ax.transAxes, color="#f8fafc", fontsize=20, fontweight="bold", ha="center")
ax.text(0.5, 0.925, "Client-Server (3-Tier) Architecture with Micro-Modular Spring Boot Backend & React Vite SPA",
        transform=ax.transAxes, color="#94a3b8", fontsize=11, ha="center")

# Outer Docker Container
docker_box = patches.FancyBboxPatch((0.03, 0.05), 0.94, 0.84, boxstyle="round,pad=0.02,rounding_size=0.03",
                                    facecolor="#1e293b", edgecolor="#38bdf8", linestyle="--", linewidth=2.5)
ax.add_patch(docker_box)
ax.text(0.05, 0.86, "[Docker] Compose Infrastructure Boundary (Bridge Network: seproject_default)",
        color="#38bdf8", fontsize=12, fontweight="bold")

# Tier 1: Presentation Tier
tier1 = patches.FancyBboxPatch((0.06, 0.10), 0.26, 0.72, boxstyle="round,pad=0.01,rounding_size=0.02",
                               facecolor="#0c4a6e", edgecolor="#0284c7", linewidth=2)
ax.add_patch(tier1)
ax.text(0.19, 0.78, "Presentation Tier (Client)\nReact 18 + Vite (Port: 5173)",
        color="#ffffff", fontsize=13, fontweight="bold", ha="center")

# Presentation Inner Boxes
ui_box = patches.FancyBboxPatch((0.08, 0.52), 0.22, 0.22, boxstyle="round,pad=0.01",
                                facecolor="#075985", edgecolor="#38bdf8", linewidth=1.5)
ax.add_patch(ui_box)
ax.text(0.09, 0.70, "Modular UI Components\n• QuestBoard.jsx\n• HeroStats.jsx (HP/XP)\n• HabitCard.jsx\n• CreateQuestModal.jsx\n• AnalyticsHeatmap.jsx\n• RewardShop.jsx",
        color="#e0f2fe", fontsize=9.5, va="top")

state_box = patches.FancyBboxPatch((0.08, 0.33), 0.22, 0.16, boxstyle="round,pad=0.01",
                                   facecolor="#075985", edgecolor="#38bdf8", linewidth=1.5)
ax.add_patch(state_box)
ax.text(0.09, 0.46, "Client State & Cache\n• React Hooks (useState/useEffect)\n• Optimistic UI Updates\n• Dark/Light Theme Context",
        color="#e0f2fe", fontsize=9.5, va="top")

api_box = patches.FancyBboxPatch((0.08, 0.14), 0.22, 0.16, boxstyle="round,pad=0.01",
                                 facecolor="#075985", edgecolor="#38bdf8", linewidth=1.5)
ax.add_patch(api_box)
ax.text(0.09, 0.27, "API Client Abstraction\n• habitService.js\n• Abstracted REST Calls\n• JWT Token Interceptor",
        color="#e0f2fe", fontsize=9.5, va="top")

# Arrow Client -> Server
ax.annotate("", xy=(0.38, 0.46), xytext=(0.32, 0.46),
            arrowprops=dict(arrowstyle="<->", color="#38bdf8", lw=3))
ax.text(0.35, 0.50, "HTTPS / JSON\nREST API\n(Port 8080)",
        color="#38bdf8", fontsize=10, fontweight="bold", ha="center")

# Tier 2: Application Tier
tier2 = patches.FancyBboxPatch((0.38, 0.10), 0.32, 0.72, boxstyle="round,pad=0.01,rounding_size=0.02",
                               facecolor="#14532d", edgecolor="#16a34a", linewidth=2)
ax.add_patch(tier2)
ax.text(0.54, 0.78, "Application Tier (Business Logic)\nSpring Boot REST API (Port: 8080)",
        color="#ffffff", fontsize=13, fontweight="bold", ha="center")

# Server Inner Boxes
ctrl_box = patches.FancyBboxPatch((0.40, 0.58), 0.28, 0.16, boxstyle="round,pad=0.01",
                                  facecolor="#166534", edgecolor="#4ade80", linewidth=1.5)
ax.add_patch(ctrl_box)
ax.text(0.41, 0.71, "REST Controllers (Separation of Concerns)\n• HabitController (/api/habits)\n• GamificationController (/api/gamification)\n• StatusController (/api/status)",
        color="#f0fdf4", fontsize=9.5, va="top")

srv_box = patches.FancyBboxPatch((0.40, 0.36), 0.28, 0.19, boxstyle="round,pad=0.01",
                                 facecolor="#166534", edgecolor="#4ade80", linewidth=1.5)
ax.add_patch(srv_box)
ax.text(0.41, 0.52, "Domain Services & Strategy (Cohesion)\n• HabitServiceImpl (Interface Abstraction)\n• GamificationService (XP/HP/Levels)\n• StreakCalculationService (SRP)\n• DailyStreakStrategy (Strategy Pattern)",
        color="#f0fdf4", fontsize=9.5, va="top")

sched_box = patches.FancyBboxPatch((0.40, 0.14), 0.28, 0.19, boxstyle="round,pad=0.01",
                                   facecolor="#166534", edgecolor="#4ade80", linewidth=1.5)
ax.add_patch(sched_box)
ax.text(0.41, 0.30, "Scheduler & Repositories (Abstraction)\n• Midnight Cron Job (Daily HP Deduction)\n• HabitRepository Interface\n• DTO Mappings & Input Validation",
        color="#f0fdf4", fontsize=9.5, va="top")

# Arrow Server -> Database
ax.annotate("", xy=(0.76, 0.46), xytext=(0.70, 0.46),
            arrowprops=dict(arrowstyle="<->", color="#4ade80", lw=3))
ax.text(0.73, 0.50, "TCP / Mongo\nDriver\n(Port 27017)",
        color="#4ade80", fontsize=10, fontweight="bold", ha="center")

# Tier 3: Persistence Tier
tier3 = patches.FancyBboxPatch((0.76, 0.10), 0.19, 0.72, boxstyle="round,pad=0.01,rounding_size=0.02",
                               facecolor="#78350f", edgecolor="#d97706", linewidth=2)
ax.add_patch(tier3)
ax.text(0.855, 0.78, "Persistence Tier\nMongoDB (Port: 27017)",
        color="#ffffff", fontsize=13, fontweight="bold", ha="center")

db_content = patches.FancyBboxPatch((0.78, 0.14), 0.15, 0.60, boxstyle="round,pad=0.01",
                                    facecolor="#92400e", edgecolor="#f59e0b", linewidth=1.5)
ax.add_patch(db_content)
ax.text(0.79, 0.71, "NoSQL Collections\n\n• habits\n• quest title, freq, time\n• streaks (curr, max)\n• xp_reward, hp_penalty\n• status logs\n\n• users\n• credentials & profile\n• level, current/max HP\n• XP gauge & gold\n• badges & titles\n\n• daily_logs\n• daily check-in audits\n• consistency history",
        color="#fef3c7", fontsize=9.5, va="top")

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")
plt.tight_layout()
plt.savefig(output_dir / "habitforge_architecture.png", facecolor=fig.get_facecolor(), edgecolor="none")
plt.close()
print("Saved habitforge_architecture.png")

# -------------------------------------------------------------
# 2. Component Modularity & Data Flow Diagram (.drawio and .png)
# -------------------------------------------------------------
drawio_flow_xml = """<mxfile host="app.diagrams.net" modified="2026-09-10T18:00:00.000Z" agent="HabitForge Design" version="24.7.5">
  <diagram id="flow-diag" name="Component Modularity and Coupling Flow">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1200" pageHeight="800" background="#0f172a" math="0" shadow="1">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>

        <!-- Flow diagram elements -->
        <mxCell id="c1" value="UI Layer (React Component)&#xa;QuestBoard / HabitCard" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#0369a1;strokeColor=#38bdf8;fontColor=#ffffff;fontSize=13;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="60" y="80" width="220" height="80" as="geometry"/>
        </mxCell>
        <mxCell id="c2" value="API Client Abstraction&#xa;habitService.js" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#0284c7;strokeColor=#38bdf8;fontColor=#ffffff;fontSize=13;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="60" y="240" width="220" height="80" as="geometry"/>
        </mxCell>
        <mxCell id="c3" value="REST Controller (Low Coupling)&#xa;HabitController.java" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#15803d;strokeColor=#4ade80;fontColor=#ffffff;fontSize=13;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="380" y="240" width="240" height="80" as="geometry"/>
        </mxCell>
        <mxCell id="c4" value="Service Interface (Abstraction)&#xa;&lt;&lt;interface&gt;&gt; HabitService" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#166534;strokeColor=#86efac;fontColor=#ffffff;fontSize=13;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="720" y="150" width="250" height="80" as="geometry"/>
        </mxCell>
        <mxCell id="c5" value="Service Implementation&#xa;HabitServiceImpl.java" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#14532d;strokeColor=#4ade80;fontColor=#ffffff;fontSize=13;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="720" y="320" width="250" height="80" as="geometry"/>
        </mxCell>
        <mxCell id="c6" value="Domain Service (High Cohesion)&#xa;StreakCalculationService.java" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#14532d;strokeColor=#4ade80;fontColor=#ffffff;fontSize=13;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="580" y="470" width="240" height="80" as="geometry"/>
        </mxCell>
        <mxCell id="c7" value="Gamification Engine (High Cohesion)&#xa;GamificationService.java" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#14532d;strokeColor=#4ade80;fontColor=#ffffff;fontSize=13;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="880" y="470" width="240" height="80" as="geometry"/>
        </mxCell>
        <mxCell id="c8" value="Repository Abstraction&#xa;&lt;&lt;interface&gt;&gt; HabitRepository" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#b45309;strokeColor=#f59e0b;fontColor=#ffffff;fontSize=13;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="720" y="620" width="250" height="80" as="geometry"/>
        </mxCell>

        <!-- Connections -->
        <mxCell id="e1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;strokeColor=#38bdf8;strokeWidth=2;fontColor=#38bdf8;" edge="1" parent="1" source="c1" target="c2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e2" value="HTTP POST /api/habits/{id}/complete" style="edgeStyle=orthogonalEdgeStyle;rounded=1;strokeColor=#38bdf8;strokeWidth=2;fontColor=#38bdf8;fontSize=11;" edge="1" parent="1" source="c2" target="c3">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e3" value="Calls Interface" style="edgeStyle=orthogonalEdgeStyle;rounded=1;strokeColor=#4ade80;strokeWidth=2;fontColor=#4ade80;fontSize=11;" edge="1" parent="1" source="c3" target="c4">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e4" value="Implements" style="edgeStyle=orthogonalEdgeStyle;dashed=1;rounded=1;strokeColor=#86efac;strokeWidth=2;fontColor=#86efac;fontSize=11;" edge="1" parent="1" source="c5" target="c4">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e5" style="edgeStyle=orthogonalEdgeStyle;rounded=1;strokeColor=#4ade80;strokeWidth=2;" edge="1" parent="1" source="c5" target="c6">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e6" style="edgeStyle=orthogonalEdgeStyle;rounded=1;strokeColor=#4ade80;strokeWidth=2;" edge="1" parent="1" source="c5" target="c7">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="e7" style="edgeStyle=orthogonalEdgeStyle;rounded=1;strokeColor=#f59e0b;strokeWidth=2;" edge="1" parent="1" source="c5" target="c8">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
"""

(output_dir / "habitforge_component_flow.drawio").write_text(drawio_flow_xml.strip(), encoding="utf-8")
print("Saved habitforge_component_flow.drawio")

# Render High-Res PNG for Component Flow
fig2, ax2 = plt.subplots(figsize=(15, 8), dpi=200)
ax2.set_facecolor("#0f172a")
fig2.patch.set_facecolor("#0f172a")

ax2.text(0.5, 0.95, "HabitForge: Component Modularity, Cohesion & Loose Coupling Data Flow",
         transform=ax2.transAxes, color="#f8fafc", fontsize=18, fontweight="bold", ha="center")
ax2.text(0.5, 0.90, "Demonstrating Dependency Injection, Strategy Pattern, and Boundary Encapsulation",
         transform=ax2.transAxes, color="#94a3b8", fontsize=11, ha="center")

# Boxes
def draw_card(ax, x, y, w, h, title, subtitle, bg, border):
    box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.01,rounding_size=0.015",
                                 facecolor=bg, edgecolor=border, linewidth=2)
    ax.add_patch(box)
    ax.text(x + w/2, y + h*0.65, title, color="#ffffff", fontsize=11, fontweight="bold", ha="center", va="center")
    ax.text(x + w/2, y + h*0.30, subtitle, color="#cbd5e1", fontsize=9, ha="center", va="center")

draw_card(ax2, 0.04, 0.70, 0.22, 0.14, "UI Layer (React Component)", "QuestBoard / HabitCard.jsx", "#0369a1", "#38bdf8")
draw_card(ax2, 0.04, 0.44, 0.22, 0.14, "Client API Abstraction", "habitService.js (stateless calls)", "#0284c7", "#38bdf8")
draw_card(ax2, 0.33, 0.44, 0.22, 0.14, "REST Controller Layer", "HabitController.java (HTTP routing)", "#15803d", "#4ade80")
draw_card(ax2, 0.63, 0.68, 0.26, 0.14, "<<interface>> HabitService", "Business Contract (Abstraction)", "#166534", "#86efac")
draw_card(ax2, 0.63, 0.44, 0.26, 0.14, "HabitServiceImpl", "Dependency Injection (@Autowired)", "#14532d", "#4ade80")
draw_card(ax2, 0.50, 0.18, 0.21, 0.14, "StreakCalculationService", "High Cohesion (Streak logic)", "#1e3a8a", "#60a5fa")
draw_card(ax2, 0.74, 0.18, 0.22, 0.14, "GamificationService", "High Cohesion (XP/HP Engine)", "#701a75", "#f472b6")
draw_card(ax2, 0.63, -0.02, 0.26, 0.12, "<<interface>> HabitRepository", "Persistence Abstraction", "#78350f", "#f59e0b")

# Arrows
ax2.annotate("", xy=(0.15, 0.58), xytext=(0.15, 0.70), arrowprops=dict(arrowstyle="->", color="#38bdf8", lw=2.5))
ax2.annotate("", xy=(0.33, 0.51), xytext=(0.26, 0.51), arrowprops=dict(arrowstyle="->", color="#38bdf8", lw=2.5))
ax2.text(0.295, 0.54, "POST /api/habits/{id}/complete", color="#38bdf8", fontsize=8.5, ha="center", fontweight="bold")

ax2.annotate("", xy=(0.63, 0.73), xytext=(0.55, 0.53), arrowprops=dict(arrowstyle="->", color="#4ade80", lw=2))
ax2.text(0.56, 0.66, "Calls Interface", color="#86efac", fontsize=8.5, fontweight="bold")

ax2.annotate("", xy=(0.76, 0.68), xytext=(0.76, 0.58), arrowprops=dict(arrowstyle="->", linestyle="--", color="#86efac", lw=2))
ax2.text(0.79, 0.63, "Implements", color="#86efac", fontsize=8.5)

ax2.annotate("", xy=(0.60, 0.32), xytext=(0.70, 0.44), arrowprops=dict(arrowstyle="->", color="#60a5fa", lw=2))
ax2.text(0.60, 0.39, "Streak Rules", color="#60a5fa", fontsize=8.5)

ax2.annotate("", xy=(0.84, 0.32), xytext=(0.79, 0.44), arrowprops=dict(arrowstyle="->", color="#f472b6", lw=2))
ax2.text(0.85, 0.39, "Award XP/Gold", color="#f472b6", fontsize=8.5)

ax2.annotate("", xy=(0.76, 0.10), xytext=(0.76, 0.18), arrowprops=dict(arrowstyle="->", color="#f59e0b", lw=2))

ax2.set_xlim(0, 1)
ax2.set_ylim(-0.05, 1)
ax2.axis("off")
plt.tight_layout()
plt.savefig(output_dir / "habitforge_component_flow.png", facecolor=fig2.get_facecolor(), edgecolor="none")
plt.close()
print("Saved habitforge_component_flow.png")

# -------------------------------------------------------------
# 3. Class Diagram (.drawio and .png)
# -------------------------------------------------------------
drawio_class_xml = """<mxfile host="app.diagrams.net" modified="2026-09-10T18:00:00.000Z" agent="HabitForge Design" version="24.7.5">
  <diagram id="class-diag" name="HabitForge UML Class Diagram">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1200" pageHeight="800" background="#0f172a" math="0" shadow="1">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Controller -->
        <mxCell id="u_ctrl" value="HabitController&#xa;--------------------&#xa;- habitService: HabitService&#xa;--------------------&#xa;+ getHabits(): ResponseEntity&lt;List&lt;HabitResponseDto&gt;&gt;&#xa;+ completeHabit(id): ResponseEntity&lt;HabitResponseDto&gt;&#xa;+ createHabit(dto): ResponseEntity&lt;HabitResponseDto&gt;" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#1e293b;strokeColor=#38bdf8;fontColor=#f8fafc;" vertex="1" parent="1">
          <mxGeometry x="60" y="80" width="340" height="150" as="geometry"/>
        </mxCell>

        <!-- Service Interface -->
        <mxCell id="u_serv_int" value="&lt;&lt;interface&gt;&gt; HabitService&#xa;--------------------&#xa;+ createHabit(userId, dto): HabitResponseDto&#xa;+ completeHabit(habitId, userId): HabitResponseDto&#xa;+ getUserHabits(userId): List&lt;HabitResponseDto&gt;" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#1e293b;strokeColor=#4ade80;fontColor=#f8fafc;" vertex="1" parent="1">
          <mxGeometry x="500" y="80" width="320" height="130" as="geometry"/>
        </mxCell>

        <!-- Service Impl -->
        <mxCell id="u_serv_impl" value="HabitServiceImpl&#xa;--------------------&#xa;- habitRepository: HabitRepository&#xa;- streakService: StreakCalculationService&#xa;- gamificationService: GamificationService&#xa;--------------------&#xa;+ createHabit(userId, dto): HabitResponseDto&#xa;+ completeHabit(habitId, userId): HabitResponseDto" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#1e293b;strokeColor=#4ade80;fontColor=#f8fafc;" vertex="1" parent="1">
          <mxGeometry x="500" y="270" width="320" height="160" as="geometry"/>
        </mxCell>

        <!-- Strategy Interface -->
        <mxCell id="u_strat_int" value="&lt;&lt;interface&gt;&gt; StreakStrategy&#xa;--------------------&#xa;+ calculateNewStreak(habit, date): int&#xa;+ isStreakBroken(habit, date): boolean" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#1e293b;strokeColor=#60a5fa;fontColor=#f8fafc;" vertex="1" parent="1">
          <mxGeometry x="880" y="80" width="280" height="120" as="geometry"/>
        </mxCell>

        <!-- Concrete Strategy -->
        <mxCell id="u_strat_impl" value="DailyStreakStrategy&#xa;--------------------&#xa;+ calculateNewStreak(habit, date): int&#xa;+ isStreakBroken(habit, date): boolean" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#1e293b;strokeColor=#60a5fa;fontColor=#f8fafc;" vertex="1" parent="1">
          <mxGeometry x="880" y="270" width="280" height="120" as="geometry"/>
        </mxCell>

        <!-- Habit Model -->
        <mxCell id="u_model" value="Habit (Domain Entity)&#xa;--------------------&#xa;- id: String&#xa;- userId: String&#xa;- title: String&#xa;- currentStreak: int&#xa;- xpReward: int&#xa;- hpPenalty: int&#xa;- completedToday: boolean&#xa;--------------------&#xa;+ isCompletedToday(): boolean" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;fillColor=#1e293b;strokeColor=#f59e0b;fontColor=#f8fafc;" vertex="1" parent="1">
          <mxGeometry x="100" y="320" width="260" height="200" as="geometry"/>
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
"""

(output_dir / "habitforge_class_diagram.drawio").write_text(drawio_class_xml.strip(), encoding="utf-8")
print("Saved habitforge_class_diagram.drawio")

# Render High-Res PNG for Class Diagram
fig3, ax3 = plt.subplots(figsize=(15, 8), dpi=200)
ax3.set_facecolor("#0f172a")
fig3.patch.set_facecolor("#0f172a")

ax3.text(0.5, 0.95, "HabitForge: UML Class & Abstraction Architecture",
         transform=ax3.transAxes, color="#f8fafc", fontsize=18, fontweight="bold", ha="center")
ax3.text(0.5, 0.90, "Illustrating Interface Contracts, Concrete Implementations, and Strategy Pattern",
         transform=ax3.transAxes, color="#94a3b8", fontsize=11, ha="center")

def draw_uml_class(ax, x, y, w, h, header, attrs, methods, border):
    card = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.01",
                                  facecolor="#1e293b", edgecolor=border, linewidth=2)
    ax.add_patch(card)
    ax.text(x + w/2, y + h - 0.04, header, color="#f8fafc", fontsize=10.5, fontweight="bold", ha="center")
    # divider line
    ax.plot([x, x + w], [y + h - 0.065, y + h - 0.065], color=border, lw=1)
    ax.text(x + 0.015, y + h - 0.08, attrs, color="#cbd5e1", fontsize=8.5, va="top", family="monospace")
    ax.plot([x, x + w], [y + h*0.42, y + h*0.42], color=border, lw=1)
    ax.text(x + 0.015, y + h*0.38, methods, color="#cbd5e1", fontsize=8.5, va="top", family="monospace")

draw_uml_class(ax3, 0.05, 0.48, 0.26, 0.36,
               "HabitController",
               "- habitService: HabitService\n- authManager: AuthManager",
               "+ getHabits(): List<HabitDto>\n+ completeHabit(id): HabitDto\n+ createHabit(dto): HabitDto",
               "#38bdf8")

draw_uml_class(ax3, 0.37, 0.48, 0.28, 0.36,
               "<<interface>> HabitService",
               "/* Contract Definition */\n/* Decouples Client */",
               "+ createHabit(dto): HabitDto\n+ completeHabit(id, uId): HabitDto\n+ getUserHabits(uId): List<HabitDto>",
               "#4ade80")

draw_uml_class(ax3, 0.37, 0.06, 0.28, 0.36,
               "HabitServiceImpl",
               "- habitRepo: HabitRepository\n- streakService: StreakService\n- gamificationSvc: GamificationSvc",
               "+ createHabit(dto): HabitDto\n+ completeHabit(id, uId): HabitDto\n- mapToDto(habit): HabitDto",
               "#86efac")

draw_uml_class(ax3, 0.70, 0.48, 0.26, 0.36,
               "<<interface>> StreakStrategy",
               "/* Strategy Pattern Contract */\n/* Open/Closed Principle */",
               "+ calculateNewStreak(h, d): int\n+ isStreakBroken(h, d): bool",
               "#60a5fa")

draw_uml_class(ax3, 0.70, 0.06, 0.26, 0.36,
               "DailyStreakStrategy",
               "/* Implements Strategy */\n- dailyGraceHours: int",
               "+ calculateNewStreak(h, d): int\n+ isStreakBroken(h, d): bool",
               "#93c5fd")

draw_uml_class(ax3, 0.05, 0.06, 0.26, 0.36,
               "Habit (Entity Model)",
               "- id: String\n- title: String\n- currentStreak: int\n- xpReward: int\n- hpPenalty: int",
               "+ isCompletedToday(): boolean\n+ setCompletedToday(val): void\n+ calculatePenalty(): int",
               "#f59e0b")

# Connectors
ax3.annotate("", xy=(0.37, 0.66), xytext=(0.31, 0.66), arrowprops=dict(arrowstyle="->", color="#38bdf8", lw=2.5))
ax3.annotate("", xy=(0.51, 0.48), xytext=(0.51, 0.42), arrowprops=dict(arrowstyle="->", linestyle="--", color="#86efac", lw=2.5))
ax3.annotate("", xy=(0.70, 0.66), xytext=(0.65, 0.66), arrowprops=dict(arrowstyle="->", color="#60a5fa", lw=2.5))
ax3.annotate("", xy=(0.83, 0.48), xytext=(0.83, 0.42), arrowprops=dict(arrowstyle="->", linestyle="--", color="#93c5fd", lw=2.5))
ax3.annotate("", xy=(0.37, 0.24), xytext=(0.31, 0.24), arrowprops=dict(arrowstyle="->", color="#f59e0b", lw=2.5))

ax3.set_xlim(0, 1)
ax3.set_ylim(0, 1)
ax3.axis("off")
plt.tight_layout()
plt.savefig(output_dir / "habitforge_class_diagram.png", facecolor=fig3.get_facecolor(), edgecolor="none")
plt.close()
print("Saved habitforge_class_diagram.png")
