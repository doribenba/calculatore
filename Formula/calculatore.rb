class Calculatore < Formula
  desc "A simple command-line (Italian) calculator"
  homepage "https://github.com/doribenba/calculatore.git"
  url "https://github.com/doribenba/calculatore/releases/download/v1.0.0/calculatore-1.0.0.tar.gz"
  sha256 "bfb9129c594f6b41ddcd43bdc9cac3a3d7f56ac36eb87b9ace3157ec8e187fa5"

  def install
    bin.install "calculatore"
    man1.install "calculatore.1" 
  end

  test do
    system "#{bin}/calculatore", "--help"
  end
end
