<div align="center">

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!--                    HEADER ULTRA EPICO                                -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<svg width="100%" height="420" viewBox="0 0 900 420" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <!-- Fondos -->
    <radialGradient id="vortex" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#064e3b" stop-opacity="0.4"/>
      <stop offset="40%" stop-color="#0f172a" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#020617" stop-opacity="1"/>
    </radialGradient>
    <linearGradient id="beam" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#10b981" stop-opacity="0"/>
      <stop offset="50%" stop-color="#10b981" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#10b981" stop-opacity="0"/>
    </linearGradient>
    <!-- Filtros -->
    <filter id="heavyGlow">
      <feGaussianBlur stdDeviation="6" result="b1"/>
      <feGaussianBlur stdDeviation="14" result="b2"/>
      <feMerge><feMergeNode in="b2"/><feMergeNode in="b1"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="softGlow">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- Base -->
  <rect width="900" height="420" fill="#020617" rx="18"/>
  <rect width="900" height="420" fill="url(#vortex)" rx="18"/>

  <!-- Estrellas parpadeantes (múltiples) -->
  <g fill="#ffffff">
    <circle cx="50" cy="40" r="1.2" opacity="0"><animate attributeName="opacity" values="0;0.8;0" dur="3s" repeatCount="indefinite"/></circle>
    <circle cx="120" cy="80" r="0.8" opacity="0"><animate attributeName="opacity" values="0;0.6;0" dur="4.2s" begin="0.5s" repeatCount="indefinite"/></circle>
    <circle cx="200" cy="30" r="1" opacity="0"><animate attributeName="opacity" values="0;1;0" dur="2.5s" begin="1s" repeatCount="indefinite"/></circle>
    <circle cx="280" cy="70" r="0.6" opacity="0"><animate attributeName="opacity" values="0;0.7;0" dur="5s" begin="1.5s" repeatCount="indefinite"/></circle>
    <circle cx="380" cy="45" r="1.1" opacity="0"><animate attributeName="opacity" values="0;0.9;0" dur="3.5s" begin="0.2s" repeatCount="indefinite"/></circle>
    <circle cx="520" cy="35" r="0.9" opacity="0"><animate attributeName="opacity" values="0;0.5;0" dur="4s" begin="2s" repeatCount="indefinite"/></circle>
    <circle cx="650" cy="60" r="1.3" opacity="0"><animate attributeName="opacity" values="0;0.8;0" dur="2.8s" begin="0.8s" repeatCount="indefinite"/></circle>
    <circle cx="750" cy="40" r="0.7" opacity="0"><animate attributeName="opacity" values="0;0.6;0" dur="3.8s" begin="1.2s" repeatCount="indefinite"/></circle>
    <circle cx="850" cy="85" r="1" opacity="0"><animate attributeName="opacity" values="0;1;0" dur="4.5s" begin="0.3s" repeatCount="indefinite"/></circle>
    <circle cx="90" cy="120" r="0.5" opacity="0"><animate attributeName="opacity" values="0;0.7;0" dur="3.2s" begin="2.5s" repeatCount="indefinite"/></circle>
    <circle cx="820" cy="130" r="0.8" opacity="0"><animate attributeName="opacity" values="0;0.9;0" dur="2.2s" begin="1.8s" repeatCount="indefinite"/></circle>
    <circle cx="450" cy="20" r="1" opacity="0"><animate attributeName="opacity" values="0;0.6;0" dur="5.5s" begin="0.6s" repeatCount="indefinite"/></circle>
  </g>

  <!-- Constelación de líneas (estático pero elegante) -->
  <g stroke="#10b981" stroke-width="0.5" opacity="0.15" fill="none">
    <path d="M50 40 L120 80 L200 30 L280 70 L380 45"/>
    <circle cx="50" cy="40" r="2" fill="#10b981" opacity="0.4"/>
    <circle cx="120" cy="80" r="2" fill="#10b981" opacity="0.4"/>
    <circle cx="200" cy="30" r="2" fill="#10b981" opacity="0.4"/>
    <circle cx="280" cy="70" r="2" fill="#10b981" opacity="0.4"/>
    <circle cx="380" cy="45" r="2" fill="#10b981" opacity="0.4"/>
    <path d="M520 35 L650 60 L750 40 L850 85"/>
    <circle cx="520" cy="35" r="2" fill="#0ea5e9" opacity="0.4"/>
    <circle cx="650" cy="60" r="2" fill="#0ea5e9" opacity="0.4"/>
    <circle cx="750" cy="40" r="2" fill="#0ea5e9" opacity="0.4"/>
    <circle cx="850" cy="85" r="2" fill="#0ea5e9" opacity="0.4"/>
  </g>

  <!-- Rayos de luz / Aurora -->
  <polygon points="150,420 300,0 350,0 250,420" fill="url(#beam)" opacity="0.3">
    <animateTransform attributeName="transform" type="skewX" values="-5;5;-5" dur="12s" repeatCount="indefinite"/>
  </polygon>
  <polygon points="500,420 650,0 700,0 600,420" fill="url(#beam)" opacity="0.2">
    <animateTransform attributeName="transform" type="skewX" values="5;-5;5" dur="15s" repeatCount="indefinite"/>
  </polygon>

  <!-- Anillos holográficos (múltiples, contrarrotatorios) -->
  <g transform="translate(450, 200)" opacity="0.12">
    <ellipse rx="180" ry="50" stroke="#10b981" stroke-width="1.2" fill="none" stroke-dasharray="40,20,10,20">
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="20s" repeatCount="indefinite"/>
    </ellipse>
  </g>
  <g transform="translate(450, 200)" opacity="0.08">
    <ellipse rx="160" ry="42" stroke="#0ea5e9" stroke-width="1" fill="none" stroke-dasharray="15,25">
      <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="14s" repeatCount="indefinite"/>
    </ellipse>
  </g>
  <g transform="translate(450, 200)" opacity="0.1">
    <ellipse rx="200" ry="55" stroke="#8b5cf6" stroke-width="0.8" fill="none" stroke-dasharray="60,30">
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="30s" repeatCount="indefinite"/>
    </ellipse>
  </g>

  <!-- Circuitos con puntos de datos viajando -->
  <g fill="none" stroke-linecap="round" stroke-linejoin="round">
    <!-- Circuito izquierdo -->
    <path d="M20 360 h140 l30 -30 h80 l20 -20 h60" stroke="#1e293b" stroke-width="2"/>
    <path d="M20 360 h140 l30 -30 h80 l20 -20 h60" stroke="#10b981" stroke-width="2" stroke-dasharray="0,400" opacity="0.8">
      <animate attributeName="stroke-dasharray" values="0,400;400,0" dur="4s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.8;0;0.8" dur="4s" repeatCount="indefinite"/>
    </path>
    <!-- Circuito derecho -->
    <path d="M880 50 h-140 l-30 30 h-80 l-20 20 h-60" stroke="#1e293b" stroke-width="2"/>
    <path d="M880 50 h-140 l-30 30 h-80 l-20 20 h-60" stroke="#0ea5e9" stroke-width="2" stroke-dasharray="0,400" opacity="0.8">
      <animate attributeName="stroke-dasharray" values="0,400;400,0" dur="4.5s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.8;0;0.8" dur="4.5s" repeatCount="indefinite"/>
    </path>
  </g>

  <!-- Nodos de circuito brillando -->
  <g fill="#10b981">
    <circle cx="20" cy="360" r="3" opacity="0.8"><animate attributeName="r" values="3;5;3" dur="2s" repeatCount="indefinite"/></circle>
    <circle cx="170" cy="330" r="3" opacity="0.6"><animate attributeName="r" values="3;5;3" dur="2s" begin="0.5s" repeatCount="indefinite"/></circle>
    <circle cx="330" cy="310" r="3" opacity="0.7"><animate attributeName="r" values="3;5;3" dur="2s" begin="1s" repeatCount="indefinite"/></circle>
    <circle cx="880" cy="50" r="3" fill="#0ea5e9" opacity="0.8"><animate attributeName="r" values="3;5;3" dur="2s" begin="0.3s" repeatCount="indefinite"/></circle>
  </g>

  <!-- Lluvia de código / Símbolos cayendo -->
  <g font-family="monospace" font-size="10" fill="#10b981" opacity="0.3">
    <text x="40" y="0">&lt;/&gt;</text><animateTransform attributeName="transform" type="translate" values="0,0; 0,420" dur="6s" repeatCount="indefinite"/>
    <text x="150" y="0">{ }</text><animateTransform attributeName="transform" type="translate" values="0,-50; 0,470" dur="8s" begin="1s" repeatCount="indefinite"/>
    <text x="260" y="0">01</text><animateTransform attributeName="transform" type="translate" values="0,-20; 0,440" dur="5s" begin="2s" repeatCount="indefinite"/>
    <text x="360" y="0">fn()</text><animateTransform attributeName="transform" type="translate" values="0,-80; 0,500" dur="7s" begin="0.5s" repeatCount="indefinite"/>
    <text x="480" y="0">#</text><animateTransform attributeName="transform" type="translate" values="0,-30; 0,450" dur="4.5s" begin="1.5s" repeatCount="indefinite"/>
    <text x="580" y="0">[]</text><animateTransform attributeName="transform" type="translate" values="0,-60; 0,480" dur="6.5s" begin="2.5s" repeatCount="indefinite"/>
    <text x="700" y="0">;;</text><animateTransform attributeName="transform" type="translate" values="0,-10; 0,430" dur="5.5s" begin="3s" repeatCount="indefinite"/>
    <text x="800" y="0">=&gt;</text><animateTransform attributeName="transform" type="translate" values="0,-40; 0,460" dur="7.5s" begin="0.8s" repeatCount="indefinite"/>
  </g>

  <!-- Partículas ascendentes más densas -->
  <g fill="#10b981">
    <circle cx="60" cy="410" r="1.5" opacity="0"><animate attributeName="cy" values="410;10" dur="5s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;0.7;0" dur="5s" repeatCount="indefinite"/></circle>
    <circle cx="140" cy="420" r="1" opacity="0"><animate attributeName="cy" values="420;30" dur="7s" begin="1s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;0.5;0" dur="7s" begin="1s" repeatCount="indefinite"/></circle>
    <circle cx="260" cy="415" r="1.8" opacity="0"><animate attributeName="cy" values="415;20" dur="6s" begin="2s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;0.8;0" dur="6s" begin="2s" repeatCount="indefinite"/></circle>
    <circle cx="380" cy="410" r="1.2" opacity="0"><animate attributeName="cy" values="410;15" dur="5.5s" begin="0.5s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;0.6;0" dur="5.5s" begin="0.5s" repeatCount="indefinite"/></circle>
    <circle cx="500" cy="420" r="1.5" opacity="0"><animate attributeName="cy" values="420;25" dur="8s" begin="1.5s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;0.7;0" dur="8s" begin="1.5s" repeatCount="indefinite"/></circle>
    <circle cx="620" cy="410" r="1" opacity="0"><animate attributeName="cy" values="410;40" dur="6.5s" begin="2.5s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;0.5;0" dur="6.5s" begin="2.5s" repeatCount="indefinite"/></circle>
    <circle cx="740" cy="415" r="1.6" opacity="0"><animate attributeName="cy" values="415;10" dur="5s" begin="3s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;0.9;0" dur="5s" begin="3s" repeatCount="indefinite"/></circle>
    <circle cx="860" cy="420" r="1.3" opacity="0"><animate attributeName="cy" values="420;50" dur="7s" begin="0.2s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;0.6;0" dur="7s" begin="0.2s" repeatCount="indefinite"/></circle>
  </g>

  <!-- ESCANER LASER -->
  <rect x="0" y="150" width="900" height="2" fill="#10b981" opacity="0.3" filter="url(#softGlow)">
    <animate attributeName="y" values="120;320;120" dur="6s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.3;0.6;0.3" dur="6s" repeatCount="indefinite"/>
  </rect>
  <rect x="0" y="150" width="900" height="20" fill="url(#beam)" opacity="0.1">
    <animate attributeName="y" values="120;320;120" dur="6s" repeatCount="indefinite"/>
  </rect>

  <!-- ═════════════════════ NOMBRE CON GLITCH INTENSO ═════════════════════ -->
  <g font-family="'Courier New', Courier, monospace" font-weight="900" font-size="68" text-anchor="middle">
    <!-- Sombra de profundidad -->
    <text x="452" y="208" fill="#000000" opacity="0.6">ROY BARRERA</text>
    
    <!-- Glitch capa roja (desplazada erráticamente) -->
    <text x="455" y="198" fill="#ef4444" opacity="0.6" filter="url(#heavyGlow)">
      ROY BARRERA
      <animate attributeName="x" values="455;445;452;458;455;453;455" dur="0.4s" repeatCount="indefinite"/>
      <animate attributeName="y" values="198;196;200;198;197;198" dur="0.35s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.6;0;0.6;0.3;0.6" dur="0.6s" repeatCount="indefinite"/>
    </text>
    
    <!-- Glitch capa cian -->
    <text x="445" y="202" fill="#06b6d4" opacity="0.7" filter="url(#heavyGlow)">
      ROY BARRERA
      <animate attributeName="x" values="445;455;448;442;445;447;445" dur="0.45s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.7;0.2;0.7;0.5;0.7" dur="0.55s" repeatCount="indefinite"/>
    </text>
    
    <!-- Glitch capa magenta -->
    <text x="450" y="205" fill="#d946ef" opacity="0.5" filter="url(#heavyGlow)">
      ROY BARRERA
      <animate attributeName="x" values="450;440;453;457;450" dur="0.5s" repeatCount="indefinite"/>
    </text>
    
    <!-- Texto principal blanco -->
    <text x="450" y="200" fill="#f8fafc" filter="url(#heavyGlow)">
      ROY BARRERA
      <animate attributeName="opacity" values="1;0.85;1;0.9;1" dur="0.2s" repeatCount="indefinite"/>
    </text>
  </g>

  <!-- Barra bajo nombre -->
  <rect x="300" y="225" width="300" height="2" fill="#334155" opacity="0.5" rx="1"/>
  <rect x="300" y="225" width="0" height="2" fill="#10b981" rx="1" filter="url(#softGlow)">
    <animate attributeName="width" values="0;300;0" dur="3s" repeatCount="indefinite"/>
    <animate attributeName="x" values="300;300;600" dur="3s" repeatCount="indefinite"/>
  </rect>

  <!-- Subtítulo con efecto de typing en SVG -->
  <text x="450" y="265" font-family="monospace" font-size="18" fill="#94a3b8" text-anchor="middle" letter-spacing="4">
    FULL STACK DEVELOPER
  </text>
  
  <text x="450" y="295" font-family="monospace" font-size="14" fill="#10b981" text-anchor="middle">
    &lt; SYSTEM.INIT("PANAMÁ") /&gt;
    <animate attributeName="opacity" values="0.4;1;0.4" dur="2s" repeatCount="indefinite"/>
  </text>

  <!-- Cursor block parpadeante -->
  <rect x="570" y="282" width="10" height="16" fill="#10b981" filter="url(#softGlow)">
    <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/>
  </rect>

  <!-- Barra de estado inferior tipo HUD -->
  <g transform="translate(0, 360)">
    <rect x="220" y="0" width="460" height="3" fill="#1e293b" rx="1.5"/>
    <rect x="220" y="0" width="0" height="3" fill="#10b981" rx="1.5" filter="url(#softGlow)">
      <animate attributeName="width" values="0;460;0" dur="5s" repeatCount="indefinite"/>
    </rect>
    <!-- Marcadores de HUD -->
    <text x="210" y="20" font-family="monospace" font-size="10" fill="#475569" text-anchor="end">CPU</text>
    <text x="220" y="20" font-family="monospace" font-size="10" fill="#10b981">██████████</text>
    <text x="680" y="20" font-family="monospace" font-size="10" fill="#475569" text-anchor="start">MEM</text>
    <text x="600" y="20" font-family="monospace" font-size="10" fill="#10b981" text-anchor="end">██████████</text>
  </g>
</svg>

<br/>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!--                    TYPING ANIMATION MEJORADA                         -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=24&pause=700&color=10B981&center=true&vCenter=true&width=950&lines=root%40roy-barrera%3A~%23+whoami;Loading+modules...+%5BOK%5D+%F0%9F%94%8D;Backend+Architect+%F0%9F%8F%97%EF%B8%8F+%7C+Frontend+Artist+%F0%9F%8E%A8;Cybersecurity+Enthusiast+%F0%9F%94%90;Turning+coffee+into+code+%E2%98%95%EF%B8%8F%E2%9E%A1%EF%B8%8F%F0%9F%92%BB;Building+the+future%2C+one+commit+at+a+time+%F0%9F%9A%80)](https://git.io/typing-svg)

<br/>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!--                    BADGES CON ESTILO                                 -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
[![Profile Views](https://komarev.com/ghpvc/?username=Roy-x24&style=for-the-badge&color=10b981&label=PROFILE+VIEWS)](https://github.com/Roy-x24)
[![GitHub Followers](https://img.shields.io/github/followers/Roy-x24?style=for-the-badge&logo=github&color=0ea5e9&labelColor=0f172a)](https://github.com/Roy-x24?tab=followers)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0f172a)](https://www.linkedin.com/in/roy-barrera-0077b1340)
[![Location](https://img.shields.io/badge/Location-Panamá_🇵🇦-10b981?style=for-the-badge&labelColor=0f172a)](https://en.wikipedia.org/wiki/Panama)

</div>

<br/>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!--                    SEPARADOR ANIMADO                                 -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<div align="center">
<svg width="100%" height="40" viewBox="0 0 900 40" xmlns="http://www.w3.org/2000/svg">
  <line x1="0" y1="20" x2="900" y2="20" stroke="#1e293b" stroke-width="1" stroke-dasharray="8,8"/>
  <circle cx="0" cy="20" r="3" fill="#10b981" filter="url(#softGlow)">
    <animate attributeName="cx" values="0;900" dur="4s" repeatCount="indefinite"/>
  </circle>
</svg>
</div>

<br/>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!--                    TERMINAL WHOAMI ULTRA                             -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->

```bash
╔════════════════════════════════════════════════════════════════════════════════╗
║  > whoami                                                                      ║
╠════════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║   ┌───[ Roy Barrera ]─────────────────────────────────────────────────────┐   ║
║   │                                                                       │   ║
║   │   🎭 Role        Full Stack Developer & Software Architect            │   ║
║   │   🎓 Degree      Lic. Desarrollo y Gestión de Software — UTP          │   ║
║   │   📍 Location    Panamá 🇵🇦                                           │   ║
║   │   🎯 Focus       Backend · Cloud · Cybersecurity · Clean Code         │   ║
║   │   ⚡ Status       Open to collaborate on ambitious projects           │   ║
║   │                                                                       │   ║
║   └───────────────────────────────────────────────────────────────────────┘   ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝
```

```typescript
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
//  CORE_PROFILE.ts  —  System Initialization Complete
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

const ROY = {
  alias     : "Roy-x24",
  role      : "Full Stack Developer",
  location  : [9.0, -79.5],           // Panamá 🇵🇦
  status    : "Online",
  
  passions  : [
    "Backend Engineering", 
    "Software Architecture", 
    "Cloud Computing",
    "Cybersecurity"
  ],
  
  stack     : {
    frontend : ["React", "Vue.js", "Tailwind CSS", "HTML5", "CSS3"],
    backend  : ["Flask", "PHP", "REST APIs", "Java"],
    data     : ["MySQL", "SQL Server"],
    langs    : ["JavaScript", "Python", "PHP", "Java"],
    tools    : ["Git", "Linux", "Postman", "VS Code"]
  },
  
  motto     : "No solo escribo código — construyo soluciones.",
  vibe      : "☕ + 💻 = 🚀"
} as const;

// export default ROY;
```

<br/>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!--                    SEPARADOR ANIMADO                                 -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<div align="center">
<svg width="100%" height="40" viewBox="0 0 900 40" xmlns="http://www.w3.org/2000/svg">
  <line x1="0" y1="20" x2="900" y2="20" stroke="#1e293b" stroke-width="1" stroke-dasharray="8,8"/>
  <circle cx="900" cy="20" r="3" fill="#0ea5e9">
    <animate attributeName="cx" values="900;0" dur="4s" repeatCount="indefinite"/>
  </circle>
</svg>
</div>

<br/>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!--                    TECH STACK MATRIX                                 -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<div align="center">

## 🧬 `Tech Stack Matrix`

<br/>

<table width="100%">
  <tr>
    <td align="center" width="160" valign="middle">
      <img src="https://img.shields.io/badge/🎨_FRONTEND-0f172a?style=for-the-badge&logoColor=white"/>
    </td>
    <td align="center" valign="middle">
      <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB"/>
      <img src="https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vue.js&logoColor=4FC08D"/>
      <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=000"/>
      <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white"/>
      <img src="https://img.shields.io/badge/Tailwind-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white"/>
      <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
      <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>
    </td>
  </tr>
  <tr><td colspan="2"><hr style="border: 0; border-top: 1px solid #1e293b;"/></td></tr>
  <tr>
    <td align="center" width="160" valign="middle">
      <img src="https://img.shields.io/badge/⚙️_BACKEND-0f172a?style=for-the-badge&logoColor=white"/>
    </td>
    <td align="center" valign="middle">
      <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
      <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/>
      <img src="https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white"/>
      <img src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white"/>
      <img src="https://img.shields.io/badge/REST_APIs-10b981?style=for-the-badge"/>
    </td>
  </tr>
  <tr><td colspan="2"><hr style="border: 0; border-top: 1px solid #1e293b;"/></td></tr>
  <tr>
    <td align="center" width="160" valign="middle">
      <img src="https://img.shields.io/badge/🗄️_DATA_%26_OPS-0f172a?style=for-the-badge&logoColor=white"/>
    </td>
    <td align="center" valign="middle">
      <img src="https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white"/>
      <img src="https://img.shields.io/badge/SQL_Server-CC2927?style=for-the-badge&logo=microsoft-sql-server&logoColor=white"/>
      <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white"/>
      <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black"/>
      <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
      <img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"/>
      <img src="https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white"/>
    </td>
  </tr>
</table>

</div>

<br/>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!--                    SEPARADOR ANIMADO                                 -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<div align="center">
<svg width="100%" height="40" viewBox="0 0 900 40" xmlns="http://www.w3.org/2000/svg">
  <line x1="0" y1="20" x2="900" y2="20" stroke="#1e293b" stroke-width="1" stroke-dasharray="8,8"/>
  <circle cx="0" cy="20" r="3" fill="#10b981" filter="url(#softGlow)">
    <animate attributeName="cx" values="0;900" dur="3s" repeatCount="indefinite"/>
  </circle>
</svg>
</div>

<br/>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!--                    EXPERIENCE LOG                                    -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<div align="center">

## 📡 `Transmission Log`

</div>

<br/>

### 🏛 `DITIC — Universidad Tecnológica de Panamá`
**Desarrollador Web · Práctica Profesional**

> Migración de sistemas legacy a arquitectura moderna **Flask + Vue.js**. Desarrollo de componentes reutilizables, validación funcional end-to-end, documentación técnica y despliegue continuo.

```diff
+ ✅ Arquitectura MVC / API REST
+ ✅ Componentes Vue.js modulares y reutilizables
+ ✅ Ciclo completo de despliegue y DevOps básico
+ ✅ Documentación técnica y control de versiones
```

<br/>

### 🌍 `Fundación Ayudinga`
**Desarrollador Frontend · Voluntariado**

> Interfaces modernas con **React + Tailwind CSS** bajo metodología Scrum. Enfoque en modularidad, mantenibilidad y revisión continua de calidad de código.

```diff
+ ✅ Metodología Scrum / Agile
+ ✅ Diseño UI/UX responsivo y accesible
+ ✅ Clean Code & Peer Code Reviews
+ ✅ Trabajo colaborativo en equipo remoto
```

<br/>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!--                    SEPARADOR ANIMADO                                 -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<div align="center">
<svg width="100%" height="40" viewBox="0 0 900 40" xmlns="http://www.w3.org/2000/svg">
  <line x1="0" y1="20" x2="900" y2="20" stroke="#1e293b" stroke-width="1" stroke-dasharray="8,8"/>
  <circle cx="900" cy="20" r="3" fill="#0ea5e9">
    <animate attributeName="cx" values="900;0" dur="3.5s" repeatCount="indefinite"/>
  </circle>
</svg>
</div>

<br/>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!--                    GITHUB DASHBOARD                                  -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<div align="center">

## 📊 `System Analytics`

<br/>

<img height="170em" src="https://github-readme-stats.vercel.app/api?username=Roy-x24&show_icons=true&theme=transparent&hide_border=true&title_color=10b981&icon_color=10b981&text_color=e2e8f0&ring_color=10b981&border_radius=12&custom_title=GitHub%20Stats"/>
<img height="170em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Roy-x24&layout=compact&theme=transparent&hide_border=true&title_color=10b981&text_color=e2e8f0&border_radius=12&custom_title=Most%20Used%20Languages"/>

<br/><br/>

<img src="https://streak-stats.demolab.com?user=Roy-x24&theme=transparent&hide_border=true&ring=10b981&fire=f59e0b&currStreakLabel=10b981&sideLabels=e2e8f0&dates=64748b&stroke=1e293b&border_radius=12"/>

<br/><br/>

[![Trophy](https://github-profile-trophy.vercel.app/?username=Roy-x24&theme=onestar&no-frame=true&column=7&margin-w=10&margin-h=10)](https://github.com/ryo-ma/github-profile-trophy)

</div>

<br/>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!--                    CONTRIBUTION GRAPH                                -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<div align="center">

## 🔥 `Neural Activity`

![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=Roy-x24&theme=react-dark&hide_border=true&color=10b981&line=10b981&point=f59e0b&area=true&area_color=10b981&radius=12)

</div>

<br/>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!--                    SNAKE ANIMATION                                   -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<div align="center">

## 🐍 `Commit Snake`

![Snake animation](https://github.com/Roy-x24/Roy-x24/blob/output/github-contribution-grid-snake-dark.svg#gh-dark-mode-only)
![Snake animation](https://github.com/Roy-x24/Roy-x24/blob/output/github-contribution-grid-snake.svg#gh-light-mode-only)

</div>

<br/>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!--                    SKILL BARS CON SVG ANIMADO                        -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<div align="center">

## 🎯 `Skill Calibration`

<br/>

<svg width="90%" height="280" viewBox="0 0 800 280" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="barGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#10b981"/>
    </linearGradient>
    <filter id="barGlow">
      <feGaussianBlur stdDeviation="2" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  
  <!-- Fondo oscuro de panel -->
  <rect x="10" y="10" width="780" height="260" rx="12" fill="#0f172a" opacity="0.5" stroke="#1e293b" stroke-width="1"/>
  
  <!-- Skill 1: Full Stack -->
  <text x="40" y="55" font-family="monospace" font-size="14" fill="#94a3b8">⚡ Full Stack Engineering</text>
  <text x="740" y="55" font-family="monospace" font-size="14" fill="#10b981" text-anchor="end">90%</text>
  <rect x="40" y="65" width="700" height="8" rx="4" fill="#1e293b"/>
  <rect x="40" y="65" width="0" height="8" rx="4" fill="url(#barGrad)" filter="url(#barGlow)">
    <animate attributeName="width" values="0;630" dur="2s" fill="freeze"/>
  </rect>
  
  <!-- Skill 2: Architecture -->
  <text x="40" y="105" font-family="monospace" font-size="14" fill="#94a3b8">🏗️ Software Architecture</text>
  <text x="740" y="105" font-family="monospace" font-size="14" fill="#10b981" text-anchor="end">85%</text>
  <rect x="40" y="115" width="700" height="8" rx="4" fill="#1e293b"/>
  <rect x="40" y="115" width="0" height="8" rx="4" fill="url(#barGrad)" filter="url(#barGlow)">
    <animate attributeName="width" values="0;595" dur="2s" begin="0.3s" fill="freeze"/>
  </rect>
  
  <!-- Skill 3: Cloud -->
  <text x="40" y="155" font-family="monospace" font-size="14" fill="#94a3b8">☁️  Cloud Computing</text>
  <text x="740" y="155" font-family="monospace" font-size="14" fill="#10b981" text-anchor="end">70%</text>
  <rect x="40" y="165" width="700" height="8" rx="4" fill="#1e293b"/>
  <rect x="40" y="165" width="0" height="8" rx="4" fill="url(#barGrad)" filter="url(#barGlow)">
    <animate attributeName="width" values="0;490" dur="2s" begin="0.6s" fill="freeze"/>
  </rect>
  
  <!-- Skill 4: Cybersecurity -->
  <text x="40" y="205" font-family="monospace" font-size="14" fill="#94a3b8">🔒 Cybersecurity</text>
  <text x="740" y="205" font-family="monospace" font-size="14" fill="#10b981" text-anchor="end">65%</text>
  <rect x="40" y="215" width="700" height="8" rx="4" fill="#1e293b"/>
  <rect x="40" y="215" width="0" height="8" rx="4" fill="url(#barGrad)" filter="url(#barGlow)">
    <animate attributeName="width" values="0;455" dur="2s" begin="0.9s" fill="freeze"/>
  </rect>
  
  <!-- Skill 5: Problem Solving -->
  <text x="40" y="255" font-family="monospace" font-size="14" fill="#94a3b8">🧠 Problem Solving</text>
  <text x="740" y="255" font-family="monospace" font-size="14" fill="#10b981" text-anchor="end">95%</text>
  <rect x="40" y="265" width="700" height="8" rx="4" fill="#1e293b"/>
  <rect x="40" y="265" width="0" height="8" rx="4" fill="url(#barGrad)" filter="url(#barGlow)">
    <animate attributeName="width" values="0;665" dur="2s" begin="1.2s" fill="freeze"/>
  </rect>
</svg>

</div>

<br/>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!--                    SEPARADOR ANIMADO                                 -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<div align="center">
<svg width="100%" height="40" viewBox="0 0 900 40" xmlns="http://www.w3.org/2000/svg">
  <line x1="0" y1="20" x2="900" y2="20" stroke="#1e293b" stroke-width="1" stroke-dasharray="8,8"/>
  <circle cx="0" cy="20" r="3" fill="#10b981" filter="url(#softGlow)">
    <animate attributeName="cx" values="0;900" dur="4s" repeatCount="indefinite"/>
  </circle>
</svg>
</div>

<br/>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!--                    QUOTE SECTION                                     -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<div align="center">

<svg width="100%" height="120" viewBox="0 0 900 120" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="quoteBg" x1="0" y1="0" x2="900" y2="120">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
  </defs>
  <rect width="900" height="120" rx="14" fill="url(#quoteBg)" stroke="#1e293b" stroke-width="1"/>
  <!-- Comillas decorativas -->
  <text x="60" y="55" font-family="serif" font-size="60" fill="#10b981" opacity="0.3">“</text>
  <text x="840" y="95" font-family="serif" font-size="60" fill="#10b981" opacity="0.3">”</text>
  <!-- Texto -->
  <text x="450" y="58" font-family="monospace" font-size="16" fill="#e2e8f0" text-anchor="middle" font-style="italic">
    "El software no solo se programa —
  </text>
  <text x="450" y="85" font-family="monospace" font-size="16" fill="#e2e8f0" text-anchor="middle" font-style="italic">
    se diseña, se estructura y se construye para resolver problemas reales."
  </text>
</svg>

</div>

<br/>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!--                    CONTACT PROTOCOL                                  -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<div align="center">

## 📡 `Open Channel`

<br/>

<a href="mailto:roybarrera508@gmail.com">
  <img src="https://img.shields.io/badge/Gmail-roybarrera508@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0f172a"/>
</a>
<a href="https://www.linkedin.com/in/roy-barrera-0077b1340" target="_blank">
  <img src="https://img.shields.io/badge/LinkedIn-Roy%20Barrera-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0f172a"/>
</a>
<a href="https://github.com/Roy-x24">
  <img src="https://img.shields.io/badge/GitHub-Roy--x24-181717?style=for-the-badge&logo=github&logoColor=white&labelColor=0f172a"/>
</a>

<br/><br/>

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!--                    FOOTER SVG ULTRA                                  -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<svg width="100%" height="160" viewBox="0 0 900 160" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="footGrad" x1="0" y1="0" x2="0" y2="160">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
    <filter id="glow2">
      <feGaussianBlur stdDeviation="4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  
  <rect width="900" height="160" fill="url(#footGrad)" rx="14"/>
  
  <!-- Onda grande -->
  <path d="M0 100 Q 150 60, 300 100 T 600 100 T 900 100 L 900 160 L 0 160 Z" fill="#1e293b" opacity="0.35">
    <animate attributeName="d" 
      values="M0 100 Q 150 60, 300 100 T 600 100 T 900 100 L 900 160 L 0 160 Z;
              M0 100 Q 150 140, 300 100 T 600 100 T 900 100 L 900 160 L 0 160 Z;
              M0 100 Q 150 60, 300 100 T 600 100 T 900 100 L 900 160 L 0 160 Z" 
      dur="7s" repeatCount="indefinite"/>
  </path>
  
  <!-- Onda media -->
  <path d="M0 120 Q 150 90, 300 120 T 600 120 T 900 120 L 900 160 L 0 160 Z" fill="#334155" opacity="0.25">
    <animate attributeName="d" 
      values="M0 120 Q 150 90, 300 120 T 600 120 T 900 120 L 900 160 L 0 160 Z;
              M0 120 Q 150 150, 300 120 T 600 120 T 900 120 L 900 160 L 0 160 Z;
              M0 120 Q 150 90, 300 120 T 600 120 T 900 120 L 900 160 L 0 160 Z" 
      dur="9s" repeatCount="indefinite"/>
  </path>
  
  <!-- Onda pequeña -->
  <path d="M0 135 Q 150 120, 300 135 T 600 135 T 900 135 L 900 160 L 0 160 Z" fill="#475569" opacity="0.15">
    <animate attributeName="d" 
      values="M0 135 Q 150 120, 300 135 T 600 135 T 900 135 L 900 160 L 0 160 Z;
              M0 135 Q 150 145, 300 135 T 600 135 T 900 135 L 900 160 L 0 160 Z;
              M0 135 Q 150 120, 300 135 T 600 135 T 900 135 L 900 160 L 0 160 Z" 
      dur="5s" repeatCount="indefinite"/>
  </path>
  
  <!-- Partículas footer -->
  <circle cx="100" cy="140" r="1.5" fill="#10b981" opacity="0.6"><animate attributeName="cy" values="140;110" dur="4s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.6;0;0.6" dur="4s" repeatCount="indefinite"/></circle>
  <circle cx="800" cy="145" r="1.2" fill="#0ea5e9" opacity="0.5"><animate attributeName="cy" values="145;115" dur="5s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.5;0;0.5" dur="5s" repeatCount="indefinite"/></circle>
  
  <!-- Texto footer -->
  <text x="450" y="125" font-family="monospace" font-size="13" fill="#64748b" text-anchor="middle" letter-spacing="3">
    ROY BARRERA  ©  2025  —  PANAMÁ 🇵🇦
  </text>
  <text x="450" y="145" font-family="monospace" font-size="11" fill="#475569" text-anchor="middle">
    Built with passion & caffeine
  </text>
  
  <!-- Indicadores de estado -->
  <circle cx="600" cy="118" r="3" fill="#10b981" filter="url(#glow2)">
    <animate attributeName="opacity" values="1;0.3;1" dur="1.5s" repeatCount="indefinite"/>
  </circle>
  <text x="610" y="122" font-family="monospace" font-size="10" fill="#10b981">ONLINE</text>
</svg>

</div>
