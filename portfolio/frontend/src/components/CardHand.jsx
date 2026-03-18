import "./CardHand.css";

// Each hand has a fixed "messy" position on the table — absolute, like cards left mid-game
const HAND_POSITIONS = [
  // Experience — top left, slightly tilted
  {
    top: "12%", left: "3%",
    labelRot: "-2deg",
    groupRot: "3deg",
    cardAngles: [-18, -7, 4, 14],
    cardOffsets: [0, -8, -4, 2],
  },
  // About me — top right, fanned wider
  {
    top: "10%", left: "52%",
    labelRot: "2deg",
    groupRot: "-4deg",
    cardAngles: [-14, -4, 6, 16],
    cardOffsets: [4, 0, -6, 2],
  },
  // Tech stuff — bottom left, more scattered
  {
    top: "55%", left: "5%",
    labelRot: "-3deg",
    groupRot: "6deg",
    cardAngles: [-20, -6, 8],
    cardOffsets: [0, -10, 4],
  },
  // Projects — bottom right
  {
    top: "52%", left: "46%",
    labelRot: "1deg",
    groupRot: "-2deg",
    cardAngles: [-10, 6],
    cardOffsets: [-4, 8],
  },
];

export default function CardHand({ hand, index, isActive, isAnyActive, shuffled, onClick }) {
  const pos = HAND_POSITIONS[index];
  const { suit, label, cards } = hand;

  return (
    <div
      className={`hand-wrapper ${shuffled ? "hand-wrapper--in" : ""}`}
      style={{
        "--shuffle-delay": `${index * 0.15}s`,
        position: "absolute",
        top: pos.top,
        left: pos.left,
      }}
    >
      {/* Handwritten label */}
      <div
        className="hand-label"
        style={{ transform: `rotate(${pos.labelRot})` }}
      >
        {label}
      </div>

      {/* The fanned hand — clickable */}
      <button
        className={`hand-fan ${isActive ? "hand-fan--active" : ""} ${isAnyActive && !isActive ? "hand-fan--dimmed" : ""}`}
        style={{ transform: `rotate(${pos.groupRot})` }}
        onClick={onClick}
        aria-label={`Open ${label} cards`}
      >
        {cards.map((card, i) => {
          const angle = pos.cardAngles[i] ?? (i * 9 - 12);
          const yOff = pos.cardOffsets[i] ?? 0;

          return (
            <div
              key={card.id}
              className="card-slot"
              style={{
                "--angle": `${angle}deg`,
                "--y-off": `${yOff}px`,
                zIndex: i + 1,
              }}
            >
              <CardBack title={card.title} suit={suit} />
            </div>
          );
        })}
      </button>
    </div>
  );
}

function CardBack({ title, suit }) {
  return (
    <div className="card-back">
      {/* Corner pips */}
      <div className="cb-corner cb-corner--tl">
        <span className="cb-pip">{suit}</span>
      </div>
      <div className="cb-corner cb-corner--br">
        <span className="cb-pip">{suit}</span>
      </div>

      {/* Main ornate body */}
      <div className="cb-body">
        <div className="cb-outer-border">
          <div className="cb-inner-border">
            {/* Four corner flourishes */}
            <div className="cb-flourish cb-flourish--tl">✦</div>
            <div className="cb-flourish cb-flourish--tr">✦</div>
            <div className="cb-flourish cb-flourish--bl">✦</div>
            <div className="cb-flourish cb-flourish--br">✦</div>

            {/* Diagonal lattice background */}
            <div className="cb-lattice" />

            {/* Center oval with title */}
            <div className="cb-oval">
              <span className="cb-oval-suit">{suit}</span>
              <span className="cb-title">{title}</span>
              <span className="cb-oval-suit">{suit}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
