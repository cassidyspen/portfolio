import { useState } from 'react'
import { arts, makeBackPattern } from '../data/arts'

const ROTS = { 3: [-3, 0, 3], 4: [-4.5, -1.5, 1.5, 4.5] }

function getRot(index, total) {
  const rots = ROTS[total] || Array.from({ length: total }, (_, i) => (i - (total - 1) / 2) * 3)
  return rots[index] ?? 0
}

export function Card({ data, index, total }) {
  const [flipped, setFlipped] = useState(false)
  const [lifted, setLifted] = useState(false)
  const rot = getRot(index, total)

  const baseTransform = `rotate(${rot}deg)`
  const hoverTransform = `rotate(${rot * 0.3}deg) translateY(-18px)`
  const flippedTransform = `rotate(${rot * 0.3}deg) translateY(-10px)`

  let transform = baseTransform
  if (flipped) transform = flippedTransform
  else if (lifted) transform = hoverTransform

  return (
    <div
      className={`card-wrap${flipped ? ' flipped' : ''}`}
      style={{ transform, zIndex: lifted || flipped ? 10 : index + 1 }}
      onMouseEnter={() => setLifted(true)}
      onMouseLeave={() => { setLifted(false) }}
      onClick={() => setFlipped(f => !f)}
    >
      <div className="card-inner">
        {/* BACK */}
        <div className="card-back">
          <div dangerouslySetInnerHTML={{ __html: makeBackPattern() }} style={{ position: 'absolute', inset: 0 }} />
          <div className="inner-border" />
          <div className="pip-tl">{data.pip}<br />{data.suit}</div>
          <div className="back-mid">
            <div className="back-art" dangerouslySetInnerHTML={{ __html: arts[data.art] }} />
            <div className="back-title">{data.backTitle}</div>
            <div className="back-hint">tap to reveal ↻</div>
          </div>
          <div className="pip-br">{data.pip}<br />{data.suit}</div>
        </div>

        {/* FACE */}
        <div className="card-face">
          <div className="inner-border" />
          <div className="face-pip-tl">{data.pip}<br />{data.suit}</div>
          <div className="face-body">
            <div className="face-art" dangerouslySetInnerHTML={{ __html: arts[data.art] }} />
            <div className="face-title">{data.faceTitle}</div>
            <div className="face-detail">
              {data.faceDetail.map((line, i) => (
                <span key={i}>{line}{i < data.faceDetail.length - 1 && <br />}</span>
              ))}
            </div>
            <div className="face-tags">
              {data.tags.map(t => <span key={t} className="face-tag">{t}</span>)}
            </div>
          </div>
          <div className="face-pip-br">{data.pip}<br />{data.suit}</div>
        </div>
      </div>
    </div>
  )
}

export function Spread({ cards, label, hint }) {
  return (
    <div className="section">
      <div className="section-label">{label}</div>
      <div className="section-hint">{hint || 'hover to lift · tap to reveal'}</div>
      <div className="spread">
        {cards.map((card, i) => (
          <Card key={i} data={card} index={i} total={cards.length} />
        ))}
      </div>
    </div>
  )
}
