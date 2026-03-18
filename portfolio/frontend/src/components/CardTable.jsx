import { useState, useEffect } from "react";
import { hands } from "../data/cards";
import CardHand from "./CardHand";
import CardModal from "./CardModal";
import CardDeck from "./CardDeck";
import "./CardTable.css";

export default function CardTable() {
  const [activeHand, setActiveHand] = useState(null);
  const [animating, setAnimating] = useState(false);
  const [shuffled, setShuffled] = useState(false);

  useEffect(() => {
    const t = setTimeout(() => setShuffled(true), 200);
    return () => clearTimeout(t);
  }, []);

  const handleHandClick = (handId) => {
    if (animating) return;
    if (activeHand === handId) { handleClose(); return; }
    setAnimating(true);
    setActiveHand(handId);
    setTimeout(() => setAnimating(false), 800);
  };

  const handleClose = () => {
    if (animating) return;
    setAnimating(true);
    setActiveHand(null);
    setTimeout(() => setAnimating(false), 800);
  };

  const activeHandData = hands.find((h) => h.id === activeHand);

  return (
    <div className="table-root">
      <header className="table-header">
        <h1 className="name-title">Cassidy Spencer</h1>
        <p className="name-subtitle">SOFTWARE ENGINEER &nbsp;|&nbsp; PITTSBURGH</p>
      </header>

      <div className={`table-scene ${activeHand ? "table-scene--blurred" : ""}`}>
        {hands.map((hand, i) => (
          <CardHand
            key={hand.id}
            hand={hand}
            index={i}
            isActive={activeHand === hand.id}
            isAnyActive={!!activeHand}
            shuffled={shuffled}
            onClick={() => handleHandClick(hand.id)}
          />
        ))}
        <CardDeck />
      </div>

      {activeHandData && (
        <CardModal hand={activeHandData} onClose={handleClose} />
      )}
    </div>
  );
}
