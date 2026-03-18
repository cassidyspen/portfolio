import { useEffect, useRef } from "react";
import CardFront from "./CardFront";
import "./CardModal.css";

export default function CardModal({ hand, onClose }) {
  const overlayRef = useRef(null);

  useEffect(() => {
    const handleKeyDown = (e) => { if (e.key === "Escape") onClose(); };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [onClose]);

  return (
    <div
      ref={overlayRef}
      className="modal-overlay"
      onClick={(e) => { if (e.target === overlayRef.current) onClose(); }}
      role="dialog"
      aria-label={`${hand.label} cards`}
    >
      <div className="modal-container">
        <div className="modal-header">
          <span className="modal-suit">{hand.suit}</span>
          <h2 className="modal-title">{hand.label}</h2>
          <button className="modal-close" onClick={onClose} aria-label="Close">✕</button>
        </div>
        <div className="modal-cards" style={{ "--card-count": hand.cards.length }}>
          {hand.cards.map((card, i) => (
            <div key={card.id} className="modal-card-wrapper" style={{ "--card-i": i }}>
              <CardFront card={card} suit={hand.suit} />
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
