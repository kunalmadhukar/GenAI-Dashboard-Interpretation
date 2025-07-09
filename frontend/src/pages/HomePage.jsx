import { useEffect, useState } from 'react'

export default function HomePage() {
  const [message, setMessage] = useState('Loading...')

  useEffect(() => {
    fetch('/api/')
      .then((r) => r.json())
      .then((data) => setMessage(data.message))
      .catch(() => setMessage('Error connecting to API'))
  }, [])

  return (
    <div>
      <h1>GenAI Dashboard UI</h1>
      <p>{message}</p>
    </div>
  )
}
