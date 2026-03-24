const img = (name) => `<img src="/flowers/${name}.png" style="width:100%;height:100%;object-fit:contain;mix-blend-mode:multiply" alt="${name}" />`

export const arts = {
  hibiscus:     img('hibiscus'),
  rose:         img('rose'),
  daisy:        img('daisy'),
  lavender:     img('lavender'),
  cosmos:       img('cosmos'),
  peony:        img('peony'),
  iris:         img('iris'),
  tulip:        img('tulip'),
  jasmine:      img('jasmine'),
  forget_me_not: img('forget_me_not'),
  buttercup:    img('buttercup'),
  anemone:      img('anemone'),
  sunflower:    img('sunflower'),
}

let _pid = 0
export function makeBackPattern() {
  const id = 'bp' + (_pid++)
  return `<svg viewBox="0 0 146 210" style="position:absolute;inset:0;width:100%;height:100%;" xmlns="http://www.w3.org/2000/svg">
    <defs><pattern id="${id}" width="18" height="18" patternUnits="userSpaceOnUse">
      <polygon points="9,1 17,9 9,17 1,9" fill="none" stroke="rgba(143,170,120,.2)" stroke-width=".7"/>
      <circle cx="9" cy="9" r="1.1" fill="rgba(143,170,120,.15)"/>
    </pattern></defs>
    <rect x="8" y="8" width="130" height="194" rx="7" fill="url(#${id})"/>
    <rect x="8" y="8" width="130" height="194" rx="7" fill="none" stroke="rgba(160,140,80,.22)" stroke-width=".8"/>
    <circle cx="73" cy="105" r="28" fill="none" stroke="rgba(143,170,120,.28)" stroke-width=".9"/>
    <circle cx="73" cy="105" r="18" fill="none" stroke="rgba(143,170,120,.2)" stroke-width=".7"/>
    <circle cx="73" cy="105" r="4" fill="rgba(143,170,120,.35)"/>
    <g transform="translate(73,105)">${[0,45,90,135,180,225,270,315].map(a => `<ellipse cx="0" cy="-13" rx="3" ry="6.5" fill="rgba(180,210,140,.27)" transform="rotate(${a})"/>`).join('')}</g>
    <polygon points="73,13 77,17 73,21 69,17" fill="rgba(143,170,120,.27)"/>
    <polygon points="73,189 77,193 73,197 69,193" fill="rgba(143,170,120,.27)"/>
    <polygon points="13,105 17,109 13,113 9,109" fill="rgba(143,170,120,.27)"/>
    <polygon points="133,105 137,109 133,113 129,109" fill="rgba(143,170,120,.27)"/>
    <text x="11" y="24" font-size="10" font-family="Georgia,serif" fill="rgba(90,138,58,.5)" font-style="italic">C</text>
    <text x="11" y="35" font-size="9" fill="rgba(143,170,120,.42)">✿</text>
    <text x="130" y="194" font-size="10" font-family="Georgia,serif" fill="rgba(90,138,58,.5)" font-style="italic" transform="rotate(180 134 190)">C</text>
    <text x="126" y="199" font-size="9" fill="rgba(143,170,120,.42)" transform="rotate(180 132 187)">✿</text>
  </svg>`
}
