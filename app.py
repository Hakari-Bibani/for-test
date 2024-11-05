import React, { useState } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Button } from '@/components/ui/button';

const ElephantToothpasteReaction = () => {
  const [reactionState, setReactionState] = useState('ready');
  const [foamHeight, setFoamHeight] = useState(50);
  const [pouring, setPouring] = useState(false);

  // Functions for beaker and cylinder visuals
  const drawBeaker = () => {
    const rotation = pouring ? '135deg' : '0deg';
    return (
      <div style={{
        position: 'relative',
        width: '100px',
        height: '150px',
        margin: 'auto',
        marginTop: '20px',
      }}>
        <div style={{
          position: 'absolute',
          width: '80px',
          height: '120px',
          border: '3px solid #333',
          borderTop: 'none',
          background: 'transparent',
          transform: `rotate(${rotation})`,
          transformOrigin: 'bottom right',
          transition: 'transform 1s',
        }}>
          <div style={{
            position: 'absolute',
            bottom: 0,
            width: '100%',
            height: '50%',
            backgroundColor: '#ADD8E6',
            transition: 'height 2s',
          }} />
        </div>
      </div>
    );
  };

  const drawCylinder = () => {
    const colors = ['#FF6B6B', '#4ECDC4', '#45B7D1'];
    const foamColor = colors[Math.floor(Math.random() * colors.length)];
    return (
      <div style={{
        position: 'relative',
        width: '150px',
        height: '200px',
        margin: 'auto',
        marginTop: '20px',
      }}>
        <div style={{
          position: 'absolute',
          width: '120px',
          height: '180px',
          border: '3px solid #333',
          borderTop: 'none',
          background: 'transparent',
        }}>
          <div style={{
            position: 'absolute',
            bottom: 0,
            width: '100%',
            height: `${foamHeight}%`,
            background: `linear-gradient(45deg, ${foamColor}, white)`,
            transition: 'height 2s',
          }} />
        </div>
        <div style={{
          position: 'absolute',
          bottom: '-25px',
          width: '100%',
          textAlign: 'center',
        }}>
          30% KI solution
        </div>
      </div>
    );
  };

  const startExperiment = () => {
    if (reactionState === 'ready') {
      setReactionState('pouring');
      setPouring(true);
      setTimeout(() => {
        setPouring(false);
        setFoamHeight(200);
      }, 1000);
    }
  };

  return (
    <Card className="w-full max-w-2xl">
      <CardHeader>
        <CardTitle>Elephant Toothpaste Reaction</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="flex justify-center">
          {drawBeaker()}
          {drawCylinder()}
        </div>
        <div className="text-center mt-6">
          <Button onClick={startExperiment}>
            Start Experiment
          </Button>
        </div>
        {reactionState === 'pouring' && (
          <div className="bg-gray-100 p-4 rounded-md mt-6">
            <h3 className="text-center">Chemical Equation:</h3>
            <p className="text-center text-2xl">2H₂O₂ (aq) → 2H₂O (l) + O₂ (g)</p>
            <div className="text-center mt-4">
              <p>
                <b>Note:</b> For a more dramatic effect in real experiments:
                <br />
                - Add a few drops of food coloring to create colorful foam
                <br />
                - Mix in liquid soap to create more voluminous foam
                <br />
                - Always perform under proper supervision and safety conditions
              </p>
            </div>
          </div>
        )}
      </CardContent>
    </Card>
  );
};

export default ElephantToothpasteReaction;
