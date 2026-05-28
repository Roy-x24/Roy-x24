<div align="center">

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                    HEADER SVG ANIMADO                         -->
<!-- ═══════════════════════════════════════════════════════════════ -->
<svg width="100%" height="360" viewBox="0 0 800 360" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad" x1="0" y1="0" x2="800" y2="360" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#020617"/>
      <stop offset="50%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#000000"/>
    </linearGradient>
    <radialGradient id="aurora" cx="400" cy="380" r="320" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#10b981" stop-opacity="0.35"/>
      <stop offset="40%" stop-color="#0ea5e9" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>
    <filter id="neonGlow">
      <feGaussianBlur stdDeviation="4" result="blur1"/>
      <feGaussianBlur stdDeviation="10" result="blur2"/>
      <feMerge>
        <feMergeNode in="blur2"/>
        <feMergeNode in="blur1"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <linearGradient id="lineGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#10b981" stop-opacity="0"/>
      <stop offset="50%" stop-color="#10b981" stop-opacity="1"/>
      <stop offset="100%" stop-color="#10b981" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <!-- Fondo principal -->
  <rect width="800" height="360" fill="url(#bgGrad)" rx="16"/>

  <!-- Halo aurora boreal -->
  <ellipse cx="400" cy="380" rx="380" ry="140" fill="url(#aurora)">
    <animate attributeName="rx" values="380;400;380" dur="7s" repeatCount="indefinite"/>
    <animate attributeName="ry" values="140;160;140" dur="9s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.8;1;0.8" dur="5s" repeatCount="indefinite"/>
  </ellipse>

  <!-- Líneas de circuito animadas -->
  <g fill="none" stroke-linecap="round">
    <path d="M30 320 h120 l40 -40 h100" stroke="#10b981" stroke-width="1.5" opacity="0.3">
      <animate attributeName="stroke-dasharray" values="0,400;400,0" dur="3s" repeatCount="indefinite"/>
    </path>
    <path d="M770 50 h-120 l-40 40 h-100" stroke="#0ea5e9" stroke-width="1.5" opacity="0.3">
      <animate attributeName="stroke-dasharray" values="0,400;400,0" dur="3.5s" repeatCount="indefinite"/>
    </path>
    <path d="M400 360 v-60" stroke="url(#lineGrad)" stroke-width="2" opacity="0.5">
      <animate attributeName="stroke-dasharray" values="0,60;60,0" dur="2s" repeatCount="indefinite"/>
    </path>
  </g>

  <!-- Partículas / Lluvia de datos -->
  <g fill="#10b981">
    <circle cx="80" cy="340" r="1.5" opacity="0">
      <animate attributeName="cy" values="340;20" dur="4s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0;0.8;0" dur="4s" repeatCount="indefinite"/>
    </circle>
    <circle cx="720" cy="320" r="2" opacity="0">
      <animate attributeName="cy" values="320;40" dur="5.5s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0;0.7;0" dur="5.5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="250" cy="350" r="1" opacity="0">
      <animate attributeName="cy" values="350;80" dur="6s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0;0.6;0" dur="6s" repeatCount="indefinite"/>
    </circle>
    <circle cx="550" cy="340" r="1.8" opacity="0">
      <animate attributeName="cy" values="340;60" dur="5s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0;0.9;0" dur="5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="150" cy="360" r="1.2" opacity="0">
      <animate attributeName="cy" values="360;100" dur="7s" repeatCount="indefinite"/>
    </circle>
    <circle cx="650" cy="360" r="1" opacity="0">
      <animate attributeName="cy" values="360;120" dur="6.5s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Círculo decorativo rotatorio (Holograma) -->
  <g transform="translate(400, 180)" opacity="0.15">
    <circle r="150" stroke="#10b981" stroke-width="1" fill="none" stroke-dasharray="30,15,5,15"/>
    <animateTransform attributeName="transform" type="rotate" from="0 400 180" to="360 400 180" dur="25s" repeatCount="indefinite"/>
  </g>
  <g transform="translate(400, 180)" opacity="0.1">
    <circle r="130" stroke="#0ea5e9" stroke-width="1" fill="none" stroke-dasharray="10,20"/>
    <animateTransform attributeName="transform" type="rotate" from="360 400 180" to="0 400 180" dur="20s" repeatCount="indefinite"/>
  </g>

  <!-- NOMBRE CON EFECTO GLITCH -->
  <g font-family="'Courier New', Courier, monospace" font-weight="900" font-size="60" text-anchor="middle">
    <!-- Capa Cian -->
    <text x="405" y="185" fill="#00f0ff" opacity="0.7" filter="url(#neonGlow)">
      ROY BARRERA
      <animate attributeName="x" values="405;395;403;405;407;405" dur="0.25s" repeatCount="indefinite"/>
    </text>
    <!-- Capa Magenta -->
    <text x="395" y="188" fill="#ff00a0" opacity="0.7" filter="url(#neonGlow)">
      ROY BARRERA
      <animate attributeName="x" values="395;405;397;395;393;395" dur="0.35s" repeatCount="indefinite"/>
    </text>
    <!-- Capa Blanca principal -->
    <text x="400" y="186" fill="#ffffff" filter="url(#neonGlow)">
      ROY BARRERA
      <animate attributeName="opacity" values="1;0.8;1;1;0.85;1" dur="0.15s" repeatCount="indefinite"/>
    </text>
  </g>

  <!-- Subtítulo -->
  <text x="400" y="240" font-family="monospace" font-size="17" fill="#94a3b8" text-anchor="middle" letter-spacing="3">
    FULL STACK DEVELOPER
  </text>
  <text x="400" y="270" font-family="monospace" font-size="15" fill="#10b981" text-anchor="middle">
    &lt;/&gt; PANAMÁ 🇵🇦 &lt;/&gt;
    <animate attributeName="opacity" values="0;1" dur="1.5s" fill="freeze"/>
  </text>

  <!-- Cursor parpadeante tipo terminal -->
  <rect x="540" y="257" width="10" height="16" fill="#10b981" opacity="0">
    <animate attributeName="opacity" values="0;1;0" dur="1.2s" repeatCount="indefinite"/>
  </rect>

  <!-- Barra de carga animada inferior -->
  <line x1="180" y1="310" x2="620" y2="310" stroke="#1e293b" stroke-width="3" stroke-linecap="round"/>
  <line x1="180" y1="310" x2="180" y2="310" stroke="#10b981" stroke-width="3" stroke-linecap="round">
    <animate attributeName="x2" values="180;620;180" dur="4s" repeatCount="indefinite"/>
  </line>
</svg>

<br/>

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                    TYPING ANIMATION                           -->
<!-- ═══════════════════════════════════════════════════════════════ -->
[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=22&pause=800&color=10B981&center=true&vCenter=true&width=900&lines=System+initialized...;Loading+modules...+%5BOK%5D;Backend+Architect+%7C+Frontend+Artist;Cybersecurity+Enthusiast+%F0%9F%94%92;Building+the+future%2C+one+commit+at+a+time+%F0%9F%9A%80)](https://git.io/typing-svg)

<br/>

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                      BADGES RÁPIDOS                           -->
<!-- ═══════════════════════════════════════════════════════════════ -->
[![Profile Views](https://komarev.com/ghpvc/?username=Roy-x24&style=for-the-badge&color=10b981&label=PROFILE+VIEWS)](https://github.com/Roy-x24)
[![GitHub Followers](https://img.shields.io/github/followers/Roy-x24?style=for-the-badge&logo=github&color=0ea5e9&labelColor=0f172a)](https://github.com/Roy-x24?tab=followers)
[![Location](https://img.shields.io/badge/Panamá-🇵🇦-10b981?style=for-the-badge&labelColor=0f172a)](https://en.wikipedia.org/wiki/Panama)

</div>

<br/>

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                    TERMINAL WHOAMI                            -->
<!-- ═══════════════════════════════════════════════════════════════ -->
```bash
╔══════════════════════════════════════════════════════════════════════╗
║  > whoami                                                            ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║   ┌─ Roy Barrera ─────────────────────────────────────────────┐     ║
║   │  Role      : Full Stack Developer & Software Architect    │     ║
║   │  Degree    : Lic. Desarrollo y Gestión de Software — UTP  │     ║
║   │  Location  : Panamá 🇵🇦                                   │     ║
║   │  Focus     : Backend · Cloud · Cybersecurity · Clean Code │     ║
║   │  Status    : Open to collaborate on ambitious projects    │     ║
║   └───────────────────────────────────────────────────────────┘     ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

```typescript
// init_core.ts
const ROY = {
  name: "Roy Barrera",
  alias: "Roy-x24",
  role: "Full Stack Developer",
  location: [9.0, -79.5], // Panamá
  passions: ["Backend Engineering", "Software Architecture", "Cloud", "Cybersecurity"],
  stack: {
    frontend : ["React", "Vue.js", "Tailwind CSS", "HTML5", "CSS3"],
    backend  : ["Flask", "PHP", "REST APIs", "Java"],
    databases: ["MySQL", "SQL Server"],
    languages: ["JavaScript", "Python", "PHP", "Java"],
    tools    : ["Git", "Linux", "Postman", "VS Code"]
  },
  motto: "No solo escribo código — construyo soluciones.",
  vibe: "Turning coffee into scalable systems ☕➡️🚀"
} as const;
```

<br/>

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                     TECH STACK MATRIX                         -->
<!-- ═══════════════════════════════════════════════════════════════ -->
<div align="center">

## 🧬 `Tech Stack Matrix`

<table>
  <tr>
    <td align="center" width="140">
      <b>🎨 Frontend</b>
    </td>
    <td align="center">
      <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB"/>
      <img src="https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vue.js&logoColor=4FC08D"/>
      <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=000"/>
      <img src="https://img.shields.io/badge/Tailwind-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white"/>
      <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
      <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>
    </td>
  </tr>
  <tr>
    <td align="center" width="140">
      <b>⚙️ Backend</b>
    </td>
    <td align="center">
      <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
      <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/>
      <img src="https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white"/>
      <img src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white"/>
    </td>
  </tr>
  <tr>
    <td align="center" width="140">
      <b>🗄️ Data & Ops</b>
    </td>
    <td align="center">
      <img src="https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white"/>
      <img src="https://img.shields.io/badge/SQL_Server-CC2927?style=for-the-badge&logo=microsoft-sql-server&logoColor=white"/>
      <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white"/>
      <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black"/>
      <img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"/>
      <img src="https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white"/>
    </td>
  </tr>
</table>

</div>

<br/>

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                     EXPERIENCE LOG                            -->
<!-- ═══════════════════════════════════════════════════════════════ -->
<div align="center">

## 📡 `Transmission Log`

</div>

### 🏛 `DITIC — Universidad Tecnológica de Panamá`
**Desarrollador Web · Práctica Profesional**

> Migración de sistemas legacy a arquitectura moderna **Flask + Vue.js**. Desarrollo de componentes reutilizables, validación funcional end-to-end, documentación técnica y despliegue continuo.

```diff
+ Arquitectura MVC / API REST
+ Componentes Vue.js modulares
+ Ciclo completo de despliegue
```

### 🌍 `Fundación Ayudinga`
**Desarrollador Frontend · Voluntariado**

> Interfaces modernas con **React + Tailwind CSS** bajo metodología Scrum. Enfoque en modularidad, mantenibilidad y revisión continua de calidad de código.

```diff
+ Metodología Scrum / Agile
+ Diseño UI/UX responsivo
+ Clean Code & Code Reviews
```

<br/>

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                      GITHUB DASHBOARD                         -->
<!-- ═══════════════════════════════════════════════════════════════ -->
<div align="center">

## 📊 `System Analytics`

<br/>

<img height="170em" src="https://github-readme-stats.vercel.app/api?username=Roy-x24&show_icons=true&theme=transparent&hide_border=true&title_color=10b981&icon_color=10b981&text_color=e2e8f0&ring_color=10b981&border_radius=12"/>
<img height="170em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Roy-x24&layout=compact&theme=transparent&hide_border=true&title_color=10b981&text_color=e2e8f0&border_radius=12"/>

<br/><br/>

<img src="https://streak-stats.demolab.com?user=Roy-x24&theme=transparent&hide_border=true&ring=10b981&fire=f59e0b&currStreakLabel=10b981&sideLabels=e2e8f0&dates=64748b&stroke=1e293b&border_radius=12"/>

<br/><br/>

[![Trophy](https://github-profile-trophy.vercel.app/?username=Roy-x24&theme=onestar&no-frame=true&column=7&margin-w=10&margin-h=10)](https://github.com/ryo-ma/github-profile-trophy)

</div>

<br/>

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                    CONTRIBUTION GRAPH                         -->
<!-- ═══════════════════════════════════════════════════════════════ -->
<div align="center">

## 🔥 `Neural Activity`

![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=Roy-x24&theme=react-dark&hide_border=true&color=10b981&line=10b981&point=f59e0b&area=true&area_color=10b981&radius=12)

</div>

<br/>

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                     SNAKE ANIMATION                           -->
<!-- ═══════════════════════════════════════════════════════════════ -->
<div align="center">

## 🐍 `Commit Snake`

![Snake animation](https://github.com/Roy-x24/Roy-x24/blob/output/github-contribution-grid-snake-dark.svg#gh-dark-mode-only)
![Snake animation](https://github.com/Roy-x24/Roy-x24/blob/output/github-contribution-grid-snake.svg#gh-light-mode-only)

</div>

<br/>

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                     CURRENT LOADOUT                           -->
<!-- ═══════════════════════════════════════════════════════════════ -->
<div align="center">

## 🎯 `Skill Calibration`

</div>

```yaml
☁️  Cloud Computing          ████████████░░░░░░░░  70%
🔒  Cybersecurity            ███████████░░░░░░░░░  65%
🏗️  Software Architecture    ██████████████░░░░░░  85%
⚡  Full Stack Engineering   ███████████████░░░░░  90%
🧠  Problem Solving          ████████████████░░░░  95%
```

<br/>

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                     CONTACT PROTOCOL                          -->
<!-- ═══════════════════════════════════════════════════════════════ -->
<div align="center">

## 📡 `Open Channel`

<br/>

<a href="mailto:roybarrera508@gmail.com">
  <img src="https://img.shields.io/badge/roybarrera508@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0f172a"/>
</a>
<a href="https://www.linkedin.com/in/roy-barrera-0077b1340" target="_blank">
  <img src="https://img.shields.io/badge/LinkedIn-Roy%20Barrera-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0f172a"/>
</a>
<a href="https://github.com/Roy-x24">
  <img src="https://img.shields.io/badge/GitHub-Roy--x24-181717?style=for-the-badge&logo=github&logoColor=white&labelColor=0f172a"/>
</a>

<br/><br/>

> *"El software no solo se programa — se diseña, se estructura y se construye para resolver problemas reales."*

<br/>

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                    FOOTER SVG ANIMADO                         -->
<!-- ═══════════════════════════════════════════════════════════════ -->
<svg width="100%" height="140" viewBox="0 0 800 140" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="footBg" x1="0" y1="0" x2="0" y2="140">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
  </defs>
  <rect width="800" height="140" fill="url(#footBg)" rx="12"/>
  
  <!-- Onda 1 -->
  <path d="M0 80 Q 200 40, 400 80 T 800 80 L 800 140 L 0 140 Z" fill="#1e293b" opacity="0.4">
    <animate attributeName="d" 
      values="M0 80 Q 200 40, 400 80 T 800 80 L 800 140 L 0 140 Z;
              M0 80 Q 200 120, 400 80 T 800 80 L 800 140 L 0 140 Z;
              M0 80 Q 200 40, 400 80 T 800 80 L 800 140 L 0 140 Z" 
      dur="6s" repeatCount="indefinite"/>
  </path>
  
  <!-- Onda 2 -->
  <path d="M0 100 Q 200 60, 400 100 T 800 100 L 800 140 L 0 140 Z" fill="#334155" opacity="0.25">
    <animate attributeName="d" 
      values="M0 100 Q 200 60, 400 100 T 800 100 L 800 140 L 0 140 Z;
              M0 100 Q 200 140, 400 100 T 800 100 L 800 140 L 0 140 Z;
              M0 100 Q 200 60, 400 100 T 800 100 L 800 140 L 0 140 Z" 
      dur="8s" repeatCount="indefinite"/>
  </path>
  
  <!-- Texto footer -->
  <text x="400" y="125" font-family="monospace" font-size="13" fill="#64748b" text-anchor="middle" letter-spacing="2">
    ROY BARRERA © 2025 — PANAMÁ
  </text>
  
  <!-- Punto verde parpadeante -->
  <circle cx="530" cy="119" r="3" fill="#10b981">
    <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite"/>
  </circle>
</svg>

</div>
