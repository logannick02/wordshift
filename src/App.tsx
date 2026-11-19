import { useState } from 'react'
import { GuessArea } from './GuessArea/GuessArea'
import { checkLetter } from './utils/Utils';
import dailyWord from "./data/dailyWord.json";

import './App.css'

function App() {
  const [results, setResults] = useState([] as string[]); // final board values
  const endWord = dailyWord.word;
  const best = dailyWord.bestPathLength;
  const dayCount = dailyWord.day;
  const [copyText, setCopyText] = useState("");

  const handleResults = (returnValue: string[]) => {
    setResults(returnValue);

    // set the results copy text
    let tmp = `WordShift #${dayCount} ${returnValue.length}/${best}`;
    tmp += "\n";

    for (let i = 0; i < endWord.length; i++) {
      if (checkLetter(endWord, endWord[i], i)) {
        tmp += "🟩";
      } else {
          tmp += "⬜";
      }
    }

    tmp += "\n";

    for (let i = 0; i < returnValue.length; i++) {
      const word = returnValue[i];

      for (let j = 0; j < word.length; j++) {
        if (checkLetter(endWord, word[j], j)) {
          tmp += "🟩";
        } else {
          tmp += "⬜";
        }
      }

      tmp += "\n";
    }

    tmp += "Play at https://lcaraway-poople.vercel.app/"
    tmp += '\n';

    setCopyText(tmp);
  }

  const handleCopy = async () => {
    if (results.length === 0) return;

    try {
      await navigator.clipboard.writeText(copyText);
    } catch (err) {
      console.error("Failed to copy results: ", err);
    }

  };

  return (
    <div className="app-area">      
      <header>
        <h1><span style={{color: "white"}}>Word<span className="italic" style={{ color: "#6AAA64" }}>Shift</span></span></h1>
        <p className="instructions">
        Get from "WORD" to {endWord} by changing one letter at a time.
        </p>
        <span>#{dayCount}: {endWord}</span>
      </header>
      
      <hr/>

      <main>
        <GuessArea endWord={endWord} onUserWin={handleResults}/>
      </main>

      <footer>
          <ul>
            <li onClick={handleCopy}>Copy results</li>
            <li></li>
          </ul>
      </footer>
    </div>
  )
}

export default App
