"use client"

import { useState, useRef, useEffect } from "react"
import { Send, Cpu, Lightbulb, Thermometer, Music, Zap, Trash2 } from "lucide-react"
import { motion, AnimatePresence } from "framer-motion"
import QuickAction from "./quick-action"
import ChatMessage from "./chat-message"

const API_URL = "/api/chat"

export default function SmartHomeChat() {
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content: "Hola! Soy tu asistente domotico inteligente. Que necesitas hoy?",
    },
  ])
  const [input, setInput] = useState("")
  const [isLoading, setIsLoading] = useState(false)
  const messagesEndRef = useRef(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const sendMessage = async (text) => {
    if (!text.trim()) return

    const userMessage = { role: "user", content: text }
    setMessages((prev) => [...prev, userMessage])
    setInput("")
    setIsLoading(true)

    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ command: text }),
      })
      const data = await response.json()
      const assistantMessage = {
        role: "assistant",
        content: data.response,
        type: data.action_type,
      }
      setMessages((prev) => [...prev, assistantMessage])
    } catch (error) {
      console.error("Error:", error)
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: "Lo siento, hubo un problema de conexion con el servidor.",
          isError: true,
        },
      ])
    } finally {
      setIsLoading(false)
    }
  }

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault()
      sendMessage(input)
    }
  }

  return (
    <div className="min-h-screen bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-slate-900 via-dark to-black flex items-center justify-center p-4 md:p-8">
      <div className="w-full max-w-4xl grid grid-cols-1 lg:grid-cols-3 gap-6 h-[85vh]">
        {/* Left Panel: Header & Quick Actions */}
        <div className="lg:col-span-1 flex flex-col gap-6">
          <motion.div
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            className="glass p-6 rounded-2xl flex flex-col items-center text-center gap-4"
          >
            <div className="w-16 h-16 rounded-full bg-gradient-to-tr from-cyan-500 to-blue-600 flex items-center justify-center shadow-lg shadow-cyan-500/20">
              <Cpu className="w-8 h-8 text-white" />
            </div>
            <div>
              <h1 className="text-2xl font-bold text-white tracking-tight text-balance">
                SmartHome <span className="text-cyan-400">AI</span>
              </h1>
              <p className="text-slate-400 text-sm mt-1">Tu hogar, bajo control</p>
            </div>
            <div className="flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20">
              <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" aria-hidden="true" />
              <span className="text-xs text-emerald-400 font-medium">Sistema Online</span>
            </div>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.1 }}
            className="glass p-6 rounded-2xl flex-1 flex flex-col"
          >
            <h2 className="text-sm font-semibold text-slate-400 uppercase tracking-wider mb-4">
              Acciones Rapidas
            </h2>
            <div className="grid grid-cols-2 gap-3">
              <QuickAction
                icon={Lightbulb}
                label="Luces ON"
                command="enciende todas las luces"
                color="yellow"
                onSend={sendMessage}
              />
              <QuickAction
                icon={Zap}
                label="Luces OFF"
                command="apaga todas las luces"
                color="slate"
                onSend={sendMessage}
              />
              <QuickAction
                icon={Thermometer}
                label="Clima 22C"
                command="pon la temperatura a 22 grados"
                color="orange"
                onSend={sendMessage}
              />
              <QuickAction
                icon={Music}
                label="Musica"
                command="pon algo de musica"
                color="purple"
                onSend={sendMessage}
              />
            </div>
          </motion.div>
        </div>

        {/* Right Panel: Chat Interface */}
        <div className="lg:col-span-2 glass rounded-2xl flex flex-col overflow-hidden relative border border-white/5 shadow-2xl">
          {/* Messages Area */}
          <div className="flex-1 overflow-y-auto p-6 flex flex-col gap-6 scroll-smooth">
            <AnimatePresence>
              {messages.map((msg, index) => (
                <ChatMessage key={index} message={msg} />
              ))}
              {isLoading && (
                <motion.div
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  className="flex justify-start"
                >
                  <div className="bg-slate-800/50 p-4 rounded-2xl rounded-bl-none border border-slate-700/50 flex items-center gap-2">
                    <span
                      className="w-2 h-2 bg-slate-400 rounded-full animate-bounce"
                      style={{ animationDelay: "0ms" }}
                    />
                    <span
                      className="w-2 h-2 bg-slate-400 rounded-full animate-bounce"
                      style={{ animationDelay: "150ms" }}
                    />
                    <span
                      className="w-2 h-2 bg-slate-400 rounded-full animate-bounce"
                      style={{ animationDelay: "300ms" }}
                    />
                  </div>
                </motion.div>
              )}
            </AnimatePresence>
            <div ref={messagesEndRef} />
          </div>

          {/* Input Area */}
          <div className="p-4 bg-slate-900/50 backdrop-blur-md border-t border-white/5">
            <div className="relative flex items-center gap-3">
              <button
                onClick={() =>
                  setMessages([
                    {
                      role: "assistant",
                      content:
                        "Hola! Soy tu asistente domotico inteligente. Que necesitas hoy?",
                    },
                  ])
                }
                className="p-3 rounded-xl bg-slate-800 text-slate-400 hover:bg-red-500/10 hover:text-red-400 transition-all"
                title="Borrar chat"
                aria-label="Borrar historial de chat"
              >
                <Trash2 size={20} />
              </button>

              <div className="flex-1 relative">
                <label htmlFor="chat-input" className="sr-only">
                  Escribe un comando
                </label>
                <input
                  id="chat-input"
                  type="text"
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  onKeyDown={handleKeyDown}
                  placeholder="Escribe un comando... (ej: 'Enciende la luz')"
                  className="w-full bg-slate-950/50 border border-slate-700/50 text-white placeholder-slate-500 rounded-xl py-3.5 pl-5 pr-12 focus:outline-none focus:ring-2 focus:ring-cyan-500/50 focus:border-cyan-500/50 transition-all font-medium"
                  autoFocus
                  disabled={isLoading}
                />
                <div className="absolute right-2 top-1/2 -translate-y-1/2">
                  <span className="text-xs text-slate-600 hidden md:block border border-slate-800 rounded px-1.5 py-0.5">
                    Enter
                  </span>
                </div>
              </div>

              <button
                onClick={() => sendMessage(input)}
                disabled={!input.trim() || isLoading}
                className="p-3.5 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 text-white shadow-lg shadow-blue-500/20 hover:shadow-blue-500/40 hover:scale-105 active:scale-95 disabled:opacity-50 disabled:hover:scale-100 transition-all duration-200"
                aria-label="Enviar mensaje"
              >
                <Send size={20} className={isLoading ? "opacity-50" : ""} />
              </button>
            </div>
            <p className="text-center text-slate-600 text-[10px] mt-3 uppercase tracking-widest font-semibold">
              SmartHome AI - Asistente Domotico
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}
