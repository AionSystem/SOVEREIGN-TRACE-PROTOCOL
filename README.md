<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 360" width="360" height="360">
  <defs>

    <linearGradient id="goldOuter" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%"   stop-color="#D4AF37"/>
      <stop offset="30%"  stop-color="#F5E08A"/>
      <stop offset="60%"  stop-color="#C5A028"/>
      <stop offset="100%" stop-color="#8B6914"/>
    </linearGradient>

    <linearGradient id="aiCyan" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"   stop-color="#001F2E"/>
      <stop offset="30%"  stop-color="#00B4D8"/>
      <stop offset="50%"  stop-color="#48CAE4"/>
      <stop offset="70%"  stop-color="#00B4D8"/>
      <stop offset="100%" stop-color="#001F2E"/>
    </linearGradient>

    <radialGradient id="innerGlow" cx="50%" cy="35%" r="60%">
      <stop offset="0%"   stop-color="#D4AF37" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#D4AF37" stop-opacity="0"/>
    </radialGradient>

    <filter id="shadowDeep" x="-20%" y="-15%" width="140%" height="140%">
      <feDropShadow dx="0" dy="8" stdDeviation="16" flood-color="#000000" flood-opacity="0.8"/>
    </filter>

    <filter id="cyanGlow">
      <feGaussianBlur in="SourceGraphic" stdDeviation="2.5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <filter id="goldGlow">
      <feGaussianBlur in="SourceGraphic" stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

  </defs>

  <!-- ═══ SHIELD — gold bevel (outer) ═══ -->
  <path d="M180,10 L340,58 L340,244 Q340,364 180,396 Q20,364 20,244 L20,58 Z"
        fill="url(#goldOuter)"
        filter="url(#shadowDeep)"/>

  <!-- ═══ SHIELD — main body (dark) ═══ -->
  <path d="M180,22 L326,64 L326,240 Q326,350 180,380 Q34,350 34,240 L34,64 Z"
        fill="#0A0C16"/>

  <!-- ═══ SHIELD — inner glow ═══ -->
  <path d="M180,22 L326,64 L326,240 Q326,350 180,380 Q34,350 34,240 L34,64 Z"
        fill="url(#innerGlow)"/>

  <!-- ═══ SHIELD — inner gold border ═══ -->
  <path d="M180,30 L314,68 L314,236 Q314,338 180,366 Q46,338 46,236 L46,68 Z"
        fill="none" stroke="url(#goldOuter)" stroke-width="1.2" opacity="0.5"/>

  <!-- ═══ GEAR / HASH — subtle engineering motif ═══ -->
  <g opacity="0.12" stroke="#D4AF37" stroke-width="1.5" fill="none">
    <circle cx="180" cy="185" r="28"/>
    <circle cx="180" cy="185" r="22"/>
    <circle cx="180" cy="185" r="16"/>
    <line x1="155" y1="185" x2="205" y2="185"/>
    <line x1="180" y1="160" x2="180" y2="210"/>
    <line x1="162" y1="167" x2="198" y2="203"/>
    <line x1="162" y1="203" x2="198" y2="167"/>
  </g>

  <!-- ═══ STP — main lettering ═══ -->
  <text x="180" y="240"
        font-family="'Georgia', 'Times New Roman', serif"
        font-size="128" font-weight="bold"
        fill="url(#goldOuter)"
        text-anchor="middle"
        letter-spacing="-5"
        filter="url(#goldGlow)">STP</text>

  <!-- ═══ CYAN LINE — under STP ═══ -->
  <rect x="68" y="258" width="224" height="3"
        fill="url(#aiCyan)"
        filter="url(#cyanGlow)"
        opacity="0.9"/>

  <!-- ═══ SOVEREIGN TRACE PROTOCOL — under cyan line ═══ -->
  <text x="180" y="285"
        font-family="'Georgia', 'Times New Roman', serif"
        font-size="12" font-weight="bold" letter-spacing="3.5"
        fill="#D4AF37" text-anchor="middle" opacity="0.85">SOVEREIGN TRACE PROTOCOL</text>

  <!-- ═══ FROZEN-4.0 — bottom label ═══ -->
  <text x="180" y="315"
        font-family="'Courier New', monospace"
        font-size="10" letter-spacing="2.5"
        fill="#48CAE4" text-anchor="middle"
        filter="url(#cyanGlow)"
        opacity="0.75">SHA-256 · FROZEN-4.0</text>

  <!-- ═══ CORNER MARKS ═══ -->
  <text x="52"  y="80" font-family="serif" font-size="8" fill="#D4AF37" opacity="0.45">✦</text>
  <text x="308" y="80" font-family="serif" font-size="8" fill="#D4AF37" opacity="0.45" text-anchor="end">✦</text>

</svg>