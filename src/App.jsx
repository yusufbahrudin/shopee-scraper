import { useState } from 'react'

export default function App() {
  const [keyword, setKeyword] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [results, setResults] = useState(null)

  // API Backend Replit
  const apiUrl = 'https://shopee-scraper--yusufbahrudin97.replit.app'

  async function handleSearch(e) {
    e.preventDefault()
    const kw = keyword.trim()
    if (!kw) return
    setLoading(true)
    setError(null)
    setResults(null)

    try {
      const res = await fetch(`${apiUrl}/api/search?keyword=${encodeURIComponent(kw)}`)
      const json = await res.json()
      if (!json.success) {
        setError(json.error || 'Terjadi kesalahan.')
      } else {
        setResults({ keyword: json.keyword, data: json.data })
      }
    } catch {
      setError('Tidak dapat terhubung ke server.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-orange-50 flex flex-col items-center px-4 py-12">

      {/* Header */}
      <div className="text-center mb-8">
        <div className="text-5xl mb-3">🛍️</div>
        <h1 className="text-3xl font-extrabold text-orange-600 mb-1">Shopee Scraper</h1>
        <p className="text-slate-500 text-sm">Cari produk termurah di Shopee berdasarkan keyword</p>
      </div>

      {/* Form */}
      <form onSubmit={handleSearch} className="w-full max-w-xl mb-10">
        <div className="flex gap-2 bg-white border border-orange-200 rounded-2xl shadow-sm p-2">
          <input
            type="text"
            value={keyword}
            onChange={e => setKeyword(e.target.value)}
            placeholder='Contoh: Compressor, Sepatu, Laptop...'
            disabled={loading}
            required
            className="flex-1 px-4 py-3 text-sm text-slate-700 placeholder-slate-400 bg-transparent outline-none"
          />
          <button
            type="submit"
            disabled={loading || !keyword.trim()}
            className="px-6 py-3 bg-orange-500 hover:bg-orange-600 disabled:bg-slate-300 disabled:cursor-not-allowed text-white text-sm font-bold rounded-xl transition-colors"
          >
            {loading ? (
              <span className="flex items-center gap-2">
                <svg className="animate-spin h-4 w-4" viewBox="0 0 24 24" fill="none">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"/>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"/>
                </svg>
                Mencari...
              </span>
            ) : 'Cari'}
          </button>
        </div>
        {loading && (
          <p className="text-center text-xs text-slate-400 mt-3 animate-pulse">
            Membuka Shopee dan mencari produk... (15–30 detik)
          </p>
        )}
      </form>

      {/* Error */}
      {error && (
        <div className="w-full max-w-xl bg-red-50 border border-red-200 rounded-2xl p-5 mb-6">
          <p className="text-red-700 font-semibold text-sm">⚠️ {error}</p>
        </div>
      )}

      {/* Results */}
      {results && (
        <div className="w-full max-w-xl">
          <p className="text-slate-500 text-sm mb-4 text-center">
            3 produk termurah untuk kata kunci: <span className="font-bold text-orange-600">"{results.keyword}"</span>
          </p>

          {results.data.length === 0 ? (
            <div className="bg-white rounded-2xl border border-slate-200 p-8 text-center text-slate-400">
              Tidak ada produk ditemukan.
            </div>
          ) : (
            <div className="flex flex-col gap-4">
              {results.data.map((p, i) => (
                <div key={i} className="bg-white rounded-2xl border border-orange-100 shadow-sm p-5 flex items-start gap-4">
                  {/* Nomor */}
                  <div className="w-9 h-9 rounded-full bg-orange-500 text-white font-extrabold text-lg flex items-center justify-center shrink-0">
                    {i + 1}
                  </div>
                  {/* Info */}
                  <div className="flex-1 min-w-0">
                    <p className="text-slate-800 font-semibold text-sm leading-snug mb-1 line-clamp-2">
                      {p.name}
                    </p>
                    <p className="text-orange-500 font-extrabold text-xl mb-2">
                      {p.price_formatted}
                    </p>
                    <a
                      href={p.link}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-xs text-blue-500 hover:text-blue-700 underline break-all"
                    >
                      {p.link}
                    </a>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {/* Empty state */}
      {!loading && !error && !results && (
        <div className="text-center text-slate-400 mt-8">
          <div className="text-5xl mb-3">🔍</div>
          <p className="text-sm">Masukkan keyword di atas untuk mulai mencari</p>
        </div>
      )}
    </div>
  )
}
