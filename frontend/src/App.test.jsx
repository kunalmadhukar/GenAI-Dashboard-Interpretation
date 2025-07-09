import { render, screen } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import { describe, it, expect, vi } from 'vitest'
import App from './App'

describe('App', () => {
  it('renders home page and fetches API', async () => {
    global.fetch = vi.fn(() =>
      Promise.resolve({ json: () => Promise.resolve({ message: 'GenAI Dashboard API is up' }) })
    )
    render(
      <MemoryRouter>
        <App />
      </MemoryRouter>
    )
    expect(screen.getByText('GenAI Dashboard UI')).toBeInTheDocument()
    await screen.findByText('GenAI Dashboard API is up')
  })
})
