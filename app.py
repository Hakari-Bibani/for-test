import React, { useState, useEffect } from 'react';

const ChemicalReaction = () => {
  const [isReacting, setIsReacting] = useState(false);
  const [showEquation, setShowEquation] = useState(false);
  const [spoonRotation, setSpoonRotation] = useState(0);
  const [bubbleHeight, setBubbleHeight] = useState(0);

  const startReaction = () => {
    setIsReacting(true);
    // Animate spoon rotation
    let rotation = 0;
    const rotateInterval = setInterval(() => {
      rotation += 2;
      setSpoonRotation(rotation);
      if (rotation >= 135) {
        clearInterval(rotateInterval);
        // Start bubble animation after spoon is rotated
        let height = 0;
        const bubbleInterval = setInterval(() => {
          height += 2;
          setBubbleHeight(height);
          if (height >= 100) {
            clearInterval(bubbleInterval);
            setShowEquation(true);
          }
        }, 50);
      }
    }, 20);
  };

  return (
    <div className="flex flex-col items-center p-8 bg-gray-50 min-h-screen">
      <h1 className="text-4xl font-bold mb-8 text-blue-600 animate-bounce">
        Baking Soda and Vinegar Reaction
      </h1>

      <div className="relative w-64 h-96">
        {/* Beaker */}
        <div className="absolute bottom-0 left-1/2 -translate-x-1/2 w-48 h-64 border-4 border-gray-400 rounded-b-lg bg-red-50">
          {/* Vinegar Text */}
          <div className="absolute top-1/2 left-1/2 -translate-x-1/2 text-lg font-mono">
            CH₃COOH
          </div>
        </div>

        {/* Spoon with powder */}
        <div 
          className="absolute top-0 left-1/2 -translate-x-1/2 transition-transform duration-1000"
          style={{ transform: `rotate(${spoonRotation}deg)` }}
        >
          <div className="w-32 h-8 bg-gray-400 rounded-full relative">
            <div className="absolute top-0 left-1/2 -translate-x-1/2 text-sm">
              NaHCO₃
            </div>
            <div className="w-8 h-24 bg-gray-400 absolute -right-4 top-4"></div>
          </div>
        </div>

        {/* Bubbles */}
        {isReacting && (
          <div 
            className="absolute bottom-64 left-1/2 -translate-x-1/2 w-48 transition-all duration-1000"
            style={{ height: `${bubbleHeight}%` }}
          >
            <div className="w-full h-full relative overflow-hidden">
              {[...Array(20)].map((_, i) => (
                <div
                  key={i}
                  className="absolute bg-white rounded-full animate-bounce opacity-80"
                  style={{
                    width: `${Math.random() * 20 + 10}px`,
                    height: `${Math.random() * 20 + 10}px`,
                    left: `${Math.random() * 100}%`,
                    top: `${Math.random() * 100}%`,
                    animationDelay: `${Math.random() * 1000}ms`
                  }}
                />
              ))}
            </div>
          </div>
        )}
      </div>

      {!isReacting && (
        <button
          onClick={startReaction}
          className="mt-8 px-6 py-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors"
        >
          Start Experiment
        </button>
      )}

      {showEquation && (
        <div className="mt-8 p-4 bg-white rounded-lg shadow-md">
          <p className="text-lg font-mono text-center">
            NaHCO₃ (s) + CH₃COOH (aq) → CO₂ (g) + H₂O (l) + NaCH₃COO (aq)
          </p>
        </div>
      )}
    </div>
  );
};

export default ChemicalReaction;
