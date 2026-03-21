import { useState } from 'react'
import ReactDOM from 'react-dom'
import { arts, makeBackPattern } from '../data/arts'

const ROTS = { 3: [-3, 0, 3], 4: [-4.5, -1.5, 1.5, 4.5] }

function getRot(index, total) {
  const rots = ROTS[total] || Array.from({ length: total }, (_, i) => (i - (total - 1) / 2) * 3)
  return rots[index] ?? 0
}

let zTop = 10

export function Card({ data, index, total }) {
  const [flipped, setFlipped] = useState(false)
  const [lifted, setLifted] = useState(false)
  const [myZ, setMyZ] = useState(index + 1)
  const [zoomed, setZoomed] = useState(false)
  const rot = getRot(index, total)

  const rotScale = typeof window !== 'undefined' && window.innerWidth < 900 ? 0.35 : 1
  const r = rot * rotScale

  const baseTransform = `rotate(${r}deg)`
  const hoverTransform = `rotate(${r * 0.3}deg) translateY(-18px)`
  const flippedTransform = `rotate(${r * 0.3}deg) translateY(-10px)`

  let transform = baseTransform
  if (flipped) transform = flippedTransform
  else if (lifted) transform = hoverTransform

  const bringToFront = () => setMyZ(++zTop)

  const handleFocus = () => { setLifted(true); bringToFront() }
  const handleBlur  = e => { if (!e.currentTarget.contains(e.relatedTarget)) setLifted(false) }

  const handleKeyDown = e => {
    // Let native elements handle their own keys
    if (e.target.tagName === 'A' || e.target.tagName === 'BUTTON') return
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault()
      bringToFront()
      setFlipped(f => !f)
    } else if (e.key === 'Escape' && flipped) {
      setFlipped(false)
    }
  }

  const modal = zoomed ? ReactDOM.createPortal(
    <div className="card-modal-backdrop" onClick={() => setZoomed(false)}>
      <div className="card-modal" onClick={e => e.stopPropagation()}>
        <button className="card-modal-close" onClick={() => setZoomed(false)} aria-label="Close">✕</button>
        <div className="face-title">{data.faceTitle}</div>
        <div className="face-sub">{data.faceSub}</div>
        {data.faceSub2 && <div className="face-sub">{data.faceSub2}</div>}
        <div className="face-desc">{data.faceDesc}</div>
        <div className="face-tags">
          {data.tags.map(t => <span key={t} className="face-tag">{t}</span>)}
        </div>
        {data.link && (
          <a className="face-link" href={data.link} target="_blank" rel="noreferrer">
            Visit ↗
          </a>
        )}
      </div>
    </div>,
    document.body
  ) : null

  return (
    <>
      <div
        className={`card-wrap${flipped ? ' flipped' : ''}`}
        style={{ transform, zIndex: myZ }}
        tabIndex={0}
        role="button"
        aria-pressed={flipped}
        aria-label={flipped ? `${data.faceTitle}: ${data.faceDesc}` : `Reveal ${data.backTitle}`}
        onMouseEnter={() => { setLifted(true); bringToFront() }}
        onMouseLeave={() => setLifted(false)}
        onFocus={handleFocus}
        onBlur={handleBlur}
        onClick={() => { bringToFront(); setFlipped(f => !f) }}
        onKeyDown={handleKeyDown}
      >
        <div className="card-inner">
          {/* BACK */}
          <div className="card-back" aria-hidden={flipped}>
            <div dangerouslySetInnerHTML={{ __html: makeBackPattern() }} style={{ position: 'absolute', inset: 0 }} />
            <div className="inner-border" />
            <div className="back-mid">
              <div className="back-art" dangerouslySetInnerHTML={{ __html: arts[data.art] }} />
              <div className="back-title">{data.backTitle}</div>
              <div className="back-hint">tap to reveal ↻</div>
            </div>
          </div>

          {/* FACE */}
          <div className="card-face" aria-hidden={!flipped}>
            <div className="inner-border" />
            <div className="face-pip-tl">{data.pip}<br />{data.suit}</div>
            <div className="face-body">
              <div className="face-title">{data.faceTitle}</div>
              <div className="face-sub">{data.faceSub}</div>
              <div className="face-sub">{data.faceSub2}</div>
              <div className="face-desc">{data.faceDesc}</div>
              <div className="face-tags">
                {data.tags.map(t => <span key={t} className="face-tag">{t}</span>)}
              </div>
              {data.link && (
                <a
                  className="face-link"
                  href={data.link}
                  target="_blank"
                  rel="noreferrer"
                  tabIndex={flipped ? 0 : -1}
                  onClick={e => e.stopPropagation()}
                >
                  Visit↗
                </a>
              )}
            </div>
            <div className="face-pip-br">{data.pip}<br />{data.suit}</div>
            <button
              className="card-zoom-btn"
              tabIndex={-1}
              onClick={e => { e.stopPropagation(); setZoomed(true) }}
              aria-label="Expand card"
            >⤢</button>
          </div>
        </div>
      </div>
      {modal}
    </>
  )
}

export function Spread({ cards, label, hint, noLabel }) {
  return (
    <div className={`section${noLabel ? ' section-continuation' : ''}`}>
      {!noLabel && <div className="section-label">{label}</div>}
      {!noLabel && <div className="section-hint">{hint || 'hover or tab to lift · press to reveal'}</div>}
      <div className={`spread spread-${cards.length}`}>
        {cards.map((card, i) => (
          <Card key={i} data={card} index={i} total={cards.length} />
        ))}
      </div>
    </div>
  )
}
