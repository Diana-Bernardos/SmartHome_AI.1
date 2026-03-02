"use client"

import { motion } from "framer-motion"

export default function ChatMessage({ message }) {
  const isUser = message.role === "user"

  return (
    <motion.div
      initial={{ opacity: 0, y: 10, scale: 0.95 }}
      animate={{ opacity: 1, y: 0, scale: 1 }}
      className={`flex ${isUser ? "justify-end" : "justify-start"}`}
    >
      <div
        className={`max-w-[80%] p-4 rounded-2xl shadow-sm ${
          isUser
            ? "bg-gradient-to-br from-cyan-600 to-blue-600 text-white rounded-br-none"
            : "bg-slate-800/80 border border-slate-700 text-slate-100 rounded-bl-none"
        }`}
      >
        <p className="leading-relaxed whitespace-pre-line">{message.content}</p>
        {!isUser && (
          <div className="flex justify-end mt-1">
            <span className="text-[10px] text-slate-400 opacity-70">IA Assistant</span>
          </div>
        )}
      </div>
    </motion.div>
  )
}
