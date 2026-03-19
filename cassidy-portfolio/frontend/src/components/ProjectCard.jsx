import { useState } from 'react'
import { arts, makeBackPattern } from '../data/arts'

export default function ProjectCard({ data }) {
  const [flipped, setFlipped] = useState(false)

  return (
    <div
      className={`proj-card-wrap${flipped ? ' flipped' : ''}`}
      onClick={() => setFlipped(f => !f)}
    >
      <div className="proj-card-inner">
        {/* BACK */}
        <div className="proj-back">
          <div className="inner-border" />
          <div className="proj-pip-row">
            <div className="proj-pip">{data.pip}<br />{data.suit}</div>
            <div className="proj-pip r">{data.pip}<br />{data.suit}</div>
          </div>
          <div className="proj-back-mid">
            <div style={{ width: 52, height: 52 }} dangerouslySetInnerHTML={{ __html: arts[data.art] }} />
            <div className="back-title">{data.backTitle}</div>
            <div className="back-hint">{data.backSub}</div>
            <div className="back-hint" style={{ marginTop: 2 }}>tap to reveal ↻</div>
          </div>
          <div style={{ height: 14 }} />
        </div>

        {/* FACE */}
        <div className="proj-face">
          <div className="inner-border" />
          <div>
            <div className="pf-pip">{data.pip} {data.suit}</div>
            <div className="pf-title">{data.title}</div>
            <div className="pf-meta">{data.meta}</div>
            <div className="pf-desc">{data.desc}</div>
            <div className="pf-tags">
              {data.tags.map(t => <span key={t} className="pf-tag">{t}</span>)}
            </div>
          </div>
          {data.url !== '#' && (
            <a
              className="pf-link"
              href={data.url}
              target="_blank"
              rel="noreferrer"
              onClick={e => e.stopPropagation()}
            >
              Visit site ↗
            </a>
          )}
        </div>
      </div>
    </div>
  )
}
