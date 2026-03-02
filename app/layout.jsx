import "./globals.css"

export const metadata = {
  title: "SmartHome AI - Asistente Domotico Inteligente",
  description: "Controla tu hogar inteligente con comandos en lenguaje natural. Luces, temperatura, musica y mas.",
}

export const viewport = {
  themeColor: "#0f172a",
  width: "device-width",
  initialScale: 1,
}

export default function RootLayout({ children }) {
  return (
    <html lang="es">
      <body>{children}</body>
    </html>
  )
}
