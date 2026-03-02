"use client"

import { motion } from "framer-motion"

const colorMap = {
  yellow: { bg: "bg-yellow-500/20", text: "text-yellow-500", hover: "hover:bg-yellow-500/30" },
  slate: { bg: "bg-slate-500/20", text: "text-slate-400", hover: "hover:bg-slate-500/30" },
  orange: { bg: "bg-orange-500/20", text: "text-orange-500", hover: "hover:bg-orange-500/30" },
  purple: { bg: "bg-purple-500/20", text: "text-purple-500", hover: "hover:bg-purple-500/30" },
}

export default function QuickAction({ icon: Icon, label, command, color, onSend }) {
  const colors = colorMap[color] || colorMap.slate

  return (
    <motion.button
      whileHover={{ scale: 1.05 }}
      whileTap={{ scale: 0.95 }}
      onClick={() => onSend(command)}
      className="glass-card p-4 rounded-xl flex flex-col items-center justify-center gap-2 text-sm font-medium transition-colors group border-t border-white/5"
    >
      <div className={`p-3 rounded-full ${colors.bg} ${colors.hover} transition-all`}>
        <Icon className={`w-6 h-6 ${colors.text}`} />
      </div>
      <span className="text-gray-300 group-hover:text-white">{label}</span>
    </motion.button>
  )
}
