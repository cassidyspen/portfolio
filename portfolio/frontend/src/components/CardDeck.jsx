import "./CardDeck.css";

export default function CardDeck() {
  return (
    <div className="deck-wrapper">
      {/* Stacked loose cards peeking out */}
      <div className="deck-loose-card deck-loose--1" />
      <div className="deck-loose-card deck-loose--2" />

      {/* The box */}
      <div className="deck-box">
        <div className="deck-box__face">
          <div className="deck-box__outer">
            <div className="deck-box__inner">
              <div className="deck-box__lattice" />
              <div className="deck-box__oval">
                <span className="deck-box__suit">♠</span>
                <span className="deck-box__brand">CS</span>
                <span className="deck-box__suit">♠</span>
              </div>
            </div>
          </div>
        </div>
        {/* Side of box */}
        <div className="deck-box__side" />
      </div>

      {/* Stack of cards in front of box */}
      <div className="deck-stack">
        {[...Array(5)].map((_, i) => (
          <div key={i} className="deck-stack-card" style={{ "--si": i }} />
        ))}
      </div>
    </div>
  );
}
