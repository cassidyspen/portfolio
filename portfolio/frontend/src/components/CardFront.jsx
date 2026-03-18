import "./CardFront.css";

export default function CardFront({ card, suit }) {
  return (
    <div className="cf">
      {/* Corner pips */}
      <div className="cf-corner cf-corner--tl">
        <span className="cf-rank">{card.rank}</span>
        <span className="cf-suit-sm">{suit}</span>
      </div>
      <div className="cf-corner cf-corner--br">
        <span className="cf-rank">{card.rank}</span>
        <span className="cf-suit-sm">{suit}</span>
      </div>

      {/* Header band */}
      <div className="cf-header">
        <div className="cf-header-pattern" />
        <div className="cf-header-text">
          <span className="cf-suit-lg">{suit}</span>
          <h3 className="cf-title">{card.title}</h3>
          {card.subtitle && <p className="cf-subtitle">{card.subtitle}</p>}
          {card.dates && <p className="cf-dates">{card.dates}</p>}
        </div>
      </div>

      {/* Content */}
      <div className="cf-content">
        {card.contributions && (
          <div className="cf-section">
            <p className="cf-section-label">Key Contributions</p>
            <ul className="cf-list">
              {card.contributions.map((c, i) => <li key={i}>{c}</li>)}
            </ul>
          </div>
        )}

        {card.body && (
          <p className="cf-body">{card.body}</p>
        )}

        {card.technologies && (
          <div className="cf-section">
            <p className="cf-section-label">Technologies</p>
            <div className="cf-pills">
              {card.technologies.map((t) => (
                <span key={t} className="cf-pill">{t}</span>
              ))}
            </div>
          </div>
        )}

        {(card.liveUrl || card.githubUrl) && (
          <div className="cf-links">
            {card.liveUrl && card.liveUrl !== "#" && (
              <a href={card.liveUrl} target="_blank" rel="noopener noreferrer" className="cf-link cf-link--live">↗ Live Site</a>
            )}
            {card.githubUrl && (
              <a href={card.githubUrl} target="_blank" rel="noopener noreferrer" className="cf-link cf-link--gh">◈ GitHub</a>
            )}
          </div>
        )}

        {card.isGallery && (
          <div className="cf-gallery-note">🐱 gallery coming soon</div>
        )}
      </div>
    </div>
  );
}
