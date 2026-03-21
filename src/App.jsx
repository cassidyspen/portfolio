import { useEffect, useState } from 'react'
import { Spread } from './components/Card'

function useWideScreen() {
  const [wide, setWide] = useState(() => window.innerWidth >= 1230)
  useEffect(() => {
    const mq = window.matchMedia('(min-width: 1230px)')
    const handler = e => setWide(e.matches)
    mq.addEventListener('change', handler)
    return () => mq.removeEventListener('change', handler)
  }, [])
  return wide
}

export default function App() {
  const [data, setData] = useState(null)
  const [error, setError] = useState(null)
  const wide = useWideScreen()

  useEffect(() => {
    fetch('/api/portfolio')
      .then(r => { if (!r.ok) throw new Error(r.status); return r.json() })
      .then(setData)
      .catch(() => setError('Could not load portfolio data.'))
  }, [])

  // On mobile, body is wider than viewport — start scroll at center so
  // background extends equally in both directions when swiping.
  useEffect(() => {
    if (window.innerWidth < 900) {
      const extra = document.body.scrollWidth - window.innerWidth
      if (extra > 0) window.scrollTo({ left: extra / 2, behavior: 'instant' })
    }
  }, [data])

  if (error) return <div className="loading">{error}</div>
  if (!data)  return <div className="loading">Loading...</div>

  return (
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
          {data.contact.resume && <>
            <span className="contact-sep">·</span>
            <a className="contact-link" href={data.contact.resume} target="_blank" rel="noreferrer">Resume</a>
          </>}
        </div>
      </header>

      {/* Experience */}
      {wide
        ? <Spread cards={data.experience} label="Experience" />
        : <><Spread cards={data.experience.slice(0, 2)} label="Experience" />
            <Spread cards={data.experience.slice(2, 4)} noLabel /></>
      }

      {/* Projects */}
      <Spread cards={data.projects} label="Projects" />

      {/* Tech */}
      <Spread cards={data.tech} label="Tech Stuff" />

      {/* About Me */}
      {wide
        ? <Spread cards={data.about} label="About Me" />
        : <><Spread cards={data.about.slice(0, 2)} label="About Me" />
            <Spread cards={data.about.slice(2, 4)} noLabel /></>
      }
      <footer className="footer">
        <a className="contact-link" href="https://docs.google.com/forms/d/e/1FAIpQLScPVYlqdGVZda0mMjoYShRdFUDnkoVSTceyfL31EYMeNGGh0g/viewform?usp=dialog">
          Feedback - Thank you!
        </a>
      </footer>
    </div>
  )
}
