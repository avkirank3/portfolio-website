import { useState, useEffect } from "react";
import "./styles.css";

const apiUrl = "http://localhost:8000/api/profile/";

const defaultData = {
  profile: {
    name: "Kiran Kumar A V",
    title: "Python Django & AI Developer",
    tagline: "I design intelligent systems, clean APIs, and high-impact digital experiences.",
    email: "avkirank3@gmail.com",
    phone: "+91 63618 54442",
    linkedin: "https://www.linkedin.com/in/kiran-kumar-a-v",
  },
  stats: [
    { label: "Years Experience", value: "3+" },
    { label: "Python Projects", value: "20+" },
    { label: "AI Solutions", value: "8+" },
    { label: "Deployment Ready", value: "100%" },
  ],
  about: {
    summary: "I am a Python developer with expertise in Django, AI-driven product development, and full-stack problem solving.",
    highlights: [
      "Backend engineering with Django and REST APIs",
      "AI integrations for automation and decision support",
      "Application architecture and deployment readiness",
    ],
  },
  skills: {
    core: ["Python", "Django", "React", "REST APIs"],
    ai: ["LLM Integration", "Prompt Engineering", "Automation"],
    tools: ["Git", "Docker", "SQL", "Linux"],
  },
  experience: [
    { role: "Python / Django Developer", company: "Freelance & Product Work", period: "2022 - Present", description: "Built Python/Django apps and workflow automation." },
    { role: "AI & Automation Engineer", company: "Independent Projects", period: "2023 - Present", description: "Created AI-assisted systems and automation flows." },
  ],
  projects: [
    { title: "AI Work Assistant", type: "Python + LLM Workflow", summary: "Intelligent assistant for productivity workflows.", impact: "Improved task organization and actions.", stack: ["Python", "Django", "AI"] },
    { title: "Portfolio Platform", type: "React + Django", summary: "Premium digital portfolio for personal brand presence.", impact: "Elegant frontend and easy deployment.", stack: ["React", "Django", "REST"] },
  ],
  highlights: [
    "Strong command of Python and Django ecosystem",
    "AI-focused product thinking with practical implementation",
    "Clean API design and maintainable architecture",
  ],
  contact: {
    cta: "Open to Python/Django development, AI product work, and collaboration opportunities.",
    email: "avkirank3@gmail.com",
    phone: "+91 63618 54442",
    linkedin: "https://www.linkedin.com/in/kiran-kumar-a-v",
  },
};

function App() {
  const [data, setData] = useState(defaultData);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) throw new Error("Failed to fetch profile");
        const profileData = await response.json();
        setData(profileData);
      } catch (error) {
        console.warn("Using fallback portfolio content:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchProfile();
  }, []);

  const { profile, stats, about, skills, experience, projects, highlights, contact } = data;

  return (
    <div className="page-shell">
      <div className="ambient ambient-one" />
      <div className="ambient ambient-two" />

      <header className="topbar">
        <div className="brand-wrap">
          <span className="brand-mark">K</span>
          <span className="brand-name">{profile.name}</span>
        </div>
        <nav className="nav">
          <a href="#about">About</a>
          <a href="#experience">Experience</a>
          <a href="#projects">Projects</a>
          <a href="#contact">Contact</a>
        </nav>
      </header>

      <main>
        <section className="hero section">
          <div className="hero-copy reveal">
            <p className="eyebrow">Python Django • AI Developer</p>
            <h1>{profile.name}</h1>
            <h2>{profile.title}</h2>
            <p className="tagline">{profile.tagline}</p>
            <div className="cta-row">
              <a className="primary-btn" href="#projects">View Projects</a>
              <a className="secondary-btn" href={profile.resume || "#contact"}>Download Resume</a>
            </div>
            <div className="meta-row">
              <span>{profile.location}</span>
              <span>{profile.email}</span>
            </div>
          </div>

          <div className="hero-card reveal">
            <div className="glass-panel">
              <p className="panel-label">Core Focus</p>
              <ul>
                {highlights.map((item, index) => (
                  <li key={index}>{item}</li>
                ))}
              </ul>
            </div>
          </div>
        </section>

        <section className="stats-grid reveal">
          {stats.map((stat) => (
            <div className="stat-card" key={stat.label}>
              <strong>{stat.value}</strong>
              <span>{stat.label}</span>
            </div>
          ))}
        </section>

        <section id="about" className="section content-grid">
          <div className="section-header reveal">
            <p className="eyebrow">About</p>
            <h3>Building dependable systems and intelligent experiences.</h3>
          </div>
          <div className="about-copy reveal">
            <p>{about.summary}</p>
            <div className="chip-list">
              {about.highlights.map((item) => (
                <span key={item} className="chip">{item}</span>
              ))}
            </div>
          </div>
        </section>

        <section className="section skills-section">
          <div className="section-header reveal">
            <p className="eyebrow">Capabilities</p>
            <h3>Technical depth across backend, frontend, and AI.</h3>
          </div>

          <div className="skills-grid">
            <div className="skill-card reveal">
              <h4>Core Stack</h4>
              <div className="chip-list">
                {skills.core.map((skill) => (
                  <span className="chip" key={skill}>{skill}</span>
                ))}
              </div>
            </div>

            <div className="skill-card reveal">
              <h4>AI & Automation</h4>
              <div className="chip-list">
                {skills.ai.map((skill) => (
                  <span className="chip" key={skill}>{skill}</span>
                ))}
              </div>
            </div>

            <div className="skill-card reveal">
              <h4>Tools</h4>
              <div className="chip-list">
                {skills.tools.map((skill) => (
                  <span className="chip" key={skill}>{skill}</span>
                ))}
              </div>
            </div>
          </div>
        </section>

        <section id="experience" className="section timeline-section">
          <div className="section-header reveal">
            <p className="eyebrow">Experience</p>
            <h3>Work & project experience focused on value.</h3>
          </div>

          <div className="timeline reveal">
            {experience.map((job) => (
              <div className="timeline-item" key={`${job.company}-${job.role}`}>
                <div className="timeline-dot" />
                <div className="timeline-content">
                  <div className="timeline-head">
                    <h4>{job.role}</h4>
                    <span>{job.period}</span>
                  </div>
                  <p className="company-name">{job.company}</p>
                  <p>{job.description}</p>
                </div>
              </div>
            ))}
          </div>
        </section>

        <section id="projects" className="section">
          <div className="section-header reveal">
            <p className="eyebrow">Projects</p>
            <h3>Applied problem solving across product, data, and AI.</h3>
          </div>

          <div className="projects-grid">
            {projects.map((project) => (
              <article className="project-card reveal" key={project.title}>
                <span className="project-type">{project.type}</span>
                <h4>{project.title}</h4>
                <p>{project.summary}</p>
                <div className="project-impact">
                  <strong>Impact</strong>
                  <span>{project.impact}</span>
                </div>
                <div className="chip-list compact">
                  {project.stack.map((tag) => (
                    <span key={tag} className="chip">{tag}</span>
                  ))}
                </div>
              </article>
            ))}
          </div>
        </section>
      </main>

      <footer id="contact" className="footer reveal">
        <div className="footer-card">
          <p className="eyebrow">Contact</p>
          <h3>Let’s build something useful.</h3>
          <p>{contact.cta}</p>
          <div className="contact-links">
            <a href={`mailto:${contact.email}`}>{contact.email}</a>
            <a href={`tel:${contact.phone.replace(/\s+/g, "")}`}>{contact.phone}</a>
            <a href={contact.linkedin} target="_blank" rel="noreferrer">LinkedIn</a>
          </div>
        </div>
      </footer>

      {loading && <div className="loading-indicator">Loading portfolio...</div>}
    </div>
  );
}

export default App;
