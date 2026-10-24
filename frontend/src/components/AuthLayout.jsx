import React from 'react';
import { Link } from 'react-router-dom';
import { ArrowLeft, Layers } from 'lucide-react';

export default function AuthLayout({ children }) {
  return <main className="auth-page">
    <header className="auth-header"><Link to="/demo" className="auth-brand"><span><Layers size={22} /></span>clienthub.</Link><Link to="/demo" className="auth-back"><ArrowLeft size={15} />Back to workspace</Link></header>
    <div className="auth-content">{children}</div>
    <footer className="auth-footer">Thoughtfully organized. Effortlessly connected.</footer>
  </main>;
}
