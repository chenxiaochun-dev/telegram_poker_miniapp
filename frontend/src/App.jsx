import { useEffect, useState } from 'react'
import './App.css'

const tg = window.Telegram?.WebApp

function App() {
  const [playerName, setPlayerName] = useState('')
  const [players, setPlayers] = useState([])
  const [status, setStatus] = useState('未加入游戏')

  const user = tg?.initDataUnsafe?.user

  useEffect(() => {
    if (user?.first_name) {
      setPlayerName(user.first_name)
    }
    fetch('/players')
      .then(res => res.json())
      .then(data => setPlayers(data))
  }, [])

  const handleJoin = async () => {
    await fetch('/join', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id: user.id, name: user.first_name })
    })
    setStatus('已加入游戏')
    const res = await fetch('/players')
    setPlayers(await res.json())
  }

  const handleAction = async (action) => {
    await fetch('/action', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id: user.id, action })
    })
  }

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold">德州扑克小程序</h1>
      <p>欢迎，{playerName}</p>
      <p className="text-green-600">状态：{status}</p>

      <button onClick={handleJoin} className="mt-4 bg-blue-500 text-white px-4 py-2 rounded">
        加入游戏
      </button>

      <div className="mt-4">
        <h2 className="text-lg font-semibold">当前玩家</h2>
        <ul>
          {players.map((p, i) => <li key={i}>{p}</li>)}
        </ul>
      </div>

      <div className="mt-4 flex gap-2">
        <button onClick={() => handleAction('deal')} className="bg-yellow-500 text-white px-3 py-1 rounded">发牌</button>
        <button onClick={() => handleAction('raise')} className="bg-green-600 text-white px-3 py-1 rounded">加注</button>
        <button onClick={() => handleAction('fold')} className="bg-red-500 text-white px-3 py-1 rounded">弃牌</button>
      </div>
    </div>
  )
}

export default App
