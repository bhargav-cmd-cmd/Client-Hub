import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import AuthLayout from '../components/AuthLayout';
import { authError } from '../services/authError';
import { Lock, Mail, Loader2, KeyRound, AlertCircle } from 'lucide-react';

const Login = () => {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setIsSubmitting(true);

    try {
      await login(email, password);
      navigate('/');
    } catch (err) {
      console.error(err);
      setError(authError(err, 'Failed to sign in. Please verify your credentials and try again.'));
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <AuthLayout>
      <div className="auth-container">
        {/* Logo / Branding */}
        <div className="auth-title">
          <div className="auth-symbol">
            <KeyRound  />
          </div>
          <h1 >
            Welcome back
          </h1>
          <p >
            Access your client management workspace
          </p>
        </div>

        {/* Card */}
        <div className="auth-card">
          {error && (
            <div className="auth-alert" role="alert">
              <AlertCircle className="w-5 h-5 shrink-0 mt-0.5" />
              <span>{error}</span>
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-5">
            {/* Email Field */}
            <div>
              <label htmlFor="email" >
                Email Address
              </label>
              <div className="auth-field">
                <div className="auth-field-icon">
                  <Mail className="w-5 h-5" />
                </div>
                <input
                  id="email"
                  autoComplete="email"
                  type="email"
                  required
                  placeholder="name@company.com"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  disabled={isSubmitting}

                />
              </div>
            </div>

            {/* Password Field */}
            <div>
              <label htmlFor="password" >
                Password
              </label>
              <div className="auth-field">
                <div className="auth-field-icon">
                  <Lock className="w-5 h-5" />
                </div>
                <input
                  id="password"
                  autoComplete="current-password"
                  type="password"
                  required
                  placeholder="••••••••"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  disabled={isSubmitting}

                />
              </div>
            </div>

            {/* Submit Button */}
            <button
              type="submit"
              disabled={isSubmitting}
              className="auth-submit"
            >
              {isSubmitting ? (
                <>
                  <Loader2 className="w-5 h-5 animate-spin" />
                  <span>Signing In...</span>
                </>
              ) : (
                <span>Sign In</span>
              )}
            </button>
          </form>

          <Link to="/demo" className="auth-demo-link">Explore the demo workspace →</Link>
          {/* Bottom link */}
          <div className="auth-switch">
            Don't have an account?{' '}
            <Link to="/register" >
              Create an account
            </Link>
          </div>
        </div>
      </div>
    </AuthLayout>
  );
};

export default Login;
