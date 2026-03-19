import { useEffect, useState } from 'react'
import { Spread } from './components/Card'
import ProjectCard from './components/ProjectCard'
import DeckCorner from './components/DeckCorner'

export default function App() {
  const [data, setData] = useState(null)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetch('/api/portfolio')
      .then(r => r.json())
      .then(setData)
      .catch(() => setError('Could not load portfolio data.'))
  }, [])

  if (error) return <div className="loading">{error}</div>
  if (!data)  return <div className="loading">Loading...</div>

  return (
    <>
      <div className="page">
        {/* Header */}
        <header className="header">
          <div className="header-sprig">✦ &nbsp;✿&nbsp; ✦</div>
          <div className="header-name">{data.name}</div>
          <div className="header-sub">{data.title} &nbsp;·&nbsp; {data.location}</div>
          <div className="header-divider">
            <div className="h-line" />
            <div className="h-dot" />
            <div className="h-line r" />
          </div>
          <div className="contact-links">
            <a className="contact-link" href={data.contact.linkedin} target="_blank" rel="noreferrer">LinkedIn</a>
            <span className="contact-sep">·</span>
            <a className="contact-link" href={data.contact.github} target="_blank" rel="noreferrer">GitHub</a>
            <span className="contact-sep">·</span>
            <a className="contact-link" href={`mailto:${data.contact.email}`}>{data.contact.email}</a>
          </div>
        </header>

        {/* Experience */}
        <Spread cards={data.experience} label="Experience" />

        {/* Projects */}
        <div className="section" style={{ animationDelay: '.25s' }}>
          <div className="section-label">Projects</div>
          <div className="section-hint">tap to flip for more</div>
          <div className="proj-row">
            {data.projects.map((p, i) => <ProjectCard key={i} data={p} />)}
          </div>
        </div>

        {/* Tech */}
        <Spread cards={data.tech} label="Tech Stuff" />

        {/* About */}
        <Spread cards={data.about} label="About Me" />
      </div>

      <DeckCorner />
    </>
  )
}
