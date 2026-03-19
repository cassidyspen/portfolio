import { makeBackPattern } from '../data/arts'

export default function DeckCorner() {
  return (
    <div className="deck-corner">
      <div className="deck-wrap">
        {[0, 1, 2].map(i => (
          <div
            key={i}
            className="deck-card"
            dangerouslySetInnerHTML={{ __html: makeBackPattern() }}
          />
        ))}
      </div>
    </div>
  )
}
